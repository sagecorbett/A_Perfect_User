from flask import Flask, render_template, request
from instabot import InstagramBot
import configparser
import time
import random


from flask import Flask
app = Flask(__name__)

# Configuration for the instagram login
config = './config.ini'
cparser = configparser.ConfigParser()
cparser.read(config)

username = cparser['AUTH']['username']
password = cparser['AUTH']['password']

bot = InstagramBot(username, password)

while True:
    time.sleep(1)
    random_word = random.choice(open('./hashtags/music.txt').readlines())
    bot.search_hashtag('car')


@app.route('/followuser', methods=['POST'])
def newfollow():
    user = request.form.get('username')
    bot.follow_user(user)
    return render_template('index.html')
