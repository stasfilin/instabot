import sys
import os

sys.path.append(os.path.join(sys.path[0], '../../'))
from instabot import Bot

bot = Bot()
bot.login()
bot.like_timeline()
bot.like_user("352300017")
bot.follow_users(["352300017"])
