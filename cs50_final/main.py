from instabot import InstagramBot
import configparser
import time

if __name__ == '__main__':
    config = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config)

    username = cparser['AUTH']['username']
    password = cparser['AUTH']['password']

    ig_bot = InstagramBot(username, password)

    # Wait for page load before clicking this will be changed when bot is running 24/7
    time.sleep(2)
    # ig_bot.search_hashtag('sage')
    ig_bot.upload_photo(username, password)
