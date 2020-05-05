from instabot import InstagramBot
import random
from apscheduler.schedulers.background import BackgroundScheduler
from helper_functions import get_random_hashtag
import getpass


def main():
    """
    main will get credentials, and login/start the instagram bot. Then start a 
    scheduler of instagram events such as like photos once randomly between 1-10 
    hours, and upload a photo every 2 days
    """

    # Get credentials for instagram login
    username_or_email = input("Username or Email: ")
    password = getpass.getpass("Password:")
    bot = InstagramBot(username_or_email, password)

    # Create a new instance of background scheduler
    scheduler = BackgroundScheduler()

    # upload a photo every 2 days
    upload_new_photo = scheduler.add_job(bot.upload_photo(
        username_or_email, password), 'interval', days=2)

    # like a random photo from a random hashtag. once randomly between 1 to 10 hours.
    like_random_photos = scheduler.add_job(bot.search_hashtag, 'interval', hours=random.randint(1,10))

    scheduler.start()

if __name__ == "__main__":
    main()
