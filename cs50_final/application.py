from flask import Flask, render_template, request
from instabot import InstagramBot
import configparser
import time
import random
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from helper_functions import get_random_hashtag


app = Flask(__name__)

# Configuration for the instagram bot login
config = './config.ini'
cparser = configparser.ConfigParser()
cparser.read(config)
username = cparser['AUTH']['username']
password = cparser['AUTH']['password']
bot = InstagramBot(username, password)

# Create a new instance of background scheduler
scheduler = BackgroundScheduler()

# upload a photo every 2 days
# upload_new_photo = scheduler.add_job(bot.upload_photo(username, password), 'interval', days=2)

# like a random photo from a random hashtag. once randomly between 1 to 10 hours.
like_random_photos = scheduler.add_job(bot.search_hashtag, 'interval', hours=random.randint(1,10))

scheduler.start()

@app.route('/followuser', methods=['POST'])
def newfollow():
    user = request.form.get('username')
    bot.follow_user(user)
    return render_template('index.html')
