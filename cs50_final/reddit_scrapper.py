
import urllib.request
import time
import os

# automate the webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': './daily_image'}
chrome_options.add_experimental_option('prefs', prefs)

class reddit_scrapper:
    def __init__(self):
        # define driver
        self.driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
        self.get_image()

    def get_image(self):
        # Check if there is already a daily image saved and if there is delete it
        if os.path.exists('./daily_image/daily.jpg'):
            os.unlink('./daily_image/daily.jpg')
            
        # open up reddit to r/pics
        self.driver.get('https://www.reddit.com/r/pics/')

        # self.driver.execute_script("window.scrollTo(0, 500)")
        image_path = self.driver.find_elements_by_class_name('ImageBox-image')[0].get_attribute('src')
        urllib.request.urlretrieve(image_path, "./daily_image/daily.jpg")

# This is here for testing delete after
if __name__ == '__main__':
    red = reddit_scrapper()
    red.get_image()
