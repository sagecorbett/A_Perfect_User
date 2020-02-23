from flask import Flask, render_template, request
from instabot import InstagramBot
import configparser


from flask import Flask
app = Flask(__name__)


config = './config.ini'
cparser = configparser.ConfigParser()
cparser.read(config)

username = cparser['AUTH']['username']
password = cparser['AUTH']['password']

bot = InstagramBot(username, password)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/newfollow', methods=['POST'])
def newfollow():
    user = request.form.get('username')
    bot.follow_user(user)
    return render_template('index.html')
