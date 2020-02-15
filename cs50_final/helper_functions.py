from selenium import webdriver
from random import randint
import time


# This functions purpose is to mimic a users scroll
def scroll_helper(num, driver):
    driver.execute_script("window.scrollTo(0, {})".format(num/2))
    time.sleep(randint(1,4))
    driver.execute_script("window.scrollTo(0, {})".format(num/2))
    return