from TwitterApi import TwitterApi
from DataBase import DataBase
from datetime import datetime, timedelta
import math
import time

twitter = TwitterApi()
database = DataBase()

yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
day_before_yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
stats_yesterday = database.get_stats(yesterday)[0]
stats_day_before_yesterday = database.get_stats(day_before_yesterday)[0]
top5_trolls = database.get_top5_trolls(yesterday)
top5_victims = database.get_top5_victims(yesterday)

tweet_daily_top5_trolls=f"""Top 5 des trolls du feur de la journée du {yesterday} (sans les bots) :

1. @{top5_trolls[0][1]} ({top5_trolls[0][2]} tweets)
2. @{top5_trolls[1][1]} ({top5_trolls[1][2]} tweets)
3. @{top5_trolls[2][1]} ({top5_trolls[2][2]} tweets)
4. @{top5_trolls[3][1]} ({top5_trolls[3][2]} tweets)
5. @{top5_trolls[4][1]} ({top5_trolls[4][2]} tweets)
"""

tweet_daily_top5_victims=f"""Top 5 des victimes du feur de la journée du {yesterday} :

1. @{top5_victims[0][1]} ({top5_victims[0][2]} tweets)
2. @{top5_victims[1][1]} ({top5_victims[1][2]} tweets)
3. @{top5_victims[2][1]} ({top5_victims[2][2]} tweets)
4. @{top5_victims[3][1]} ({top5_victims[3][2]} tweets)
5. @{top5_victims[4][1]} ({top5_victims[4][2]} tweets)
"""

tweet_daily_stat = f"""Les stats de la journée du {yesterday} :

- {stats_yesterday[1]} blagues faites ({'+' if stats_yesterday[1] >= stats_day_before_yesterday[1] else '-'}{math.floor((1-(stats_yesterday[1]/stats_day_before_yesterday[1]))*100)}%)
- {stats_yesterday[3]} trolls ({'+' if stats_yesterday[3] >= stats_day_before_yesterday[3] else '-'}{math.floor((1-(stats_yesterday[3]/stats_day_before_yesterday[3]))*100)}%)
- {stats_yesterday[4]} victimes ({'+' if stats_yesterday[4] >= stats_day_before_yesterday[4] else '-'}{math.floor((1-(stats_yesterday[4]/stats_day_before_yesterday[4]))*100)}%)
- {math.floor(stats_yesterday[7]/stats_yesterday[11]*100)}% iPhones, {math.floor(stats_yesterday[6]/stats_yesterday[11]*100)}% Android, {math.floor(stats_yesterday[9]/stats_yesterday[11]*100)}% ordinateurs, {math.floor(stats_yesterday[8]/stats_yesterday[11]*100)}% iPads"""

twitter.tweet(tweet_daily_stat)
time.sleep(60)
twitter.tweet(tweet_daily_top5_trolls)
time.sleep(60)
twitter.tweet(tweet_daily_top5_victims)