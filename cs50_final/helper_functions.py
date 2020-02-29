from selenium import webdriver
import random
import time


# This functions purpose is to mimic a users scroll
def scroll_helper(num, driver):
    driver.execute_script("window.scrollTo(0, {})".format(num/2))
    time.sleep(random.randint(1,4))
    driver.execute_script("window.scrollTo(0, {})".format(num/2))
    return


# This will return a random word from a txt file of all popular hashtags
def get_random_hashtag():
    return random.choice(open('./hashtags/music.txt').read().split())






