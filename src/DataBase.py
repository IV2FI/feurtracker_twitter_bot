import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

class DataBase:
    def __init__(self):
        load_dotenv()
        self.db = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME']
        )
        self.users_table = os.environ['DB_TABLE_USERS']
        self.tweets_table = os.environ['DB_TABLE_TWEETS']
        self.stats_table = os.environ['DB_TABLE_STATS']

    def get_stats(self, day):
        self.cursor = self.db.cursor()
        sql = "SELECT *,(nb_iphone+nb_android+nb_bots+nb_computer+nb_ipad) AS total_devices  FROM " + self.stats_table + " WHERE day='"+day+"';"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_top5_trolls(self, day):
        self.cursor = self.db.cursor()
        sql = f"""select tweets.author_id, users.username, count(*) as num 
        from {self.tweets_table}
        INNER JOIN {self.users_table} ON users.user_id=tweets.author_id
        WHERE tweets.created_at LIKE "2022-03-12%" AND sent_from IN('Twitter for iPhone', 'Twitter for iPad', 'Twitter for Android', 'TweetDeck', 'Twitter Web App', 'Twitter for Mac')
        group by tweets.author_id
        order by count(*) desc
        limit 5"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_top5_victims(self, day):
        self.cursor = self.db.cursor()
        sql = f"""select tweets.victim_id, users.username, count(*) as num 
        from {self.tweets_table}
        INNER JOIN {self.users_table} ON users.user_id=tweets.victim_id
        WHERE tweets.created_at LIKE "2022-03-12%" AND sent_from IN('Twitter for iPhone', 'Twitter for iPad', 'Twitter for Android', 'TweetDeck', 'Twitter Web App', 'Twitter for Mac')
        group by tweets.victim_id
        order by count(*) desc
        limit 5"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    


