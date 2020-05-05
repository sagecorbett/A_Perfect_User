from selenium import webdriver
import random
import time


def scroll_helper(num, driver):
    """
    This functions purpose is to mimic a users scroll
    """
    driver.execute_script("window.scrollTo(0, {})".format(num/2))
    time.sleep(random.randint(1,4))
    driver.execute_script("window.scrollTo(0, {})".format(num/2))
    return


def get_random_hashtag():
    """
    This will return a random word from a txt file of all popular hashtags. 
    Used when the IG uses this hashtag bot is like a random photo.
    """
    return random.choice(open('./hashtags/music.txt').read().split())






