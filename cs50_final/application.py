from flask import Flask, render_template, request
from instabot import InstagramBot
import configparser
import time
import random
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


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
job = scheduler.add_job(bot.upload_photo(username, password), 'interval', days=2)
scheduler.start()


@app.route('/followuser', methods=['POST'])
def newfollow():
    user = request.form.get('username')
    bot.follow_user(user)
    return render_template('index.html')
