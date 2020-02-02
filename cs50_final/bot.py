
import time
import os

# file/ file path manipulation
import configparser

# automate the webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# reddit scrapper that returns a picture
from reddit_scrapper import reddit_scrapper

# We need these settings to start instagram in mobile view
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 500, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# class is a template that encapsulates various functionality that is in some way related

class InstagramBot:
    # this is a function that is called when you create an instance of a class
    # self: so that we can set various attributes to this class so that they are specific
    #  to each instance of that class
    def __init__(self, username, password):
        """
            Initializes an instance of the instagram bot class

            Args:
                username:str
                password:str

            Attributes:
                driver:selenium.webdriver.Chrome: The driver that is used to automate browser actions
        """
        # set these parameters within this class
        self.username = username
        self.password = password

        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver', chrome_options=chrome_options)

        self.login()

    def login(self):
        # Get instagram login page
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        # find username and password inputs by name
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        # Scroll the login mobile button into view
        self.driver.execute_script("window.scrollTo(0, 50)")

        # find login button by xpath
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Log In')]").click()

        # Instagram throws a lot of notifications when logging in. This will redirect to clear some
        # and cancel the others
        time.sleep(2)
        self.driver.get(self.base_url)

        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Cancel')]").click()

        time.sleep(2)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Follow')]")
        follow_button.click()

    def upload_photo(self):
        get_photo = reddit_scrapper()
        get_photo.get_image()
        # upload_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/svg')
        # upload_button.click()


#  if this is the file that is executed when you initially run the program
if __name__ == '__main__':
    config = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config)

    username = cparser['AUTH']['username']
    password = cparser['AUTH']['password']

    ig_bot = InstagramBot(username, password)
    # ig_bot.follow_user('jimmypage')
    ig_bot.upload_photo()
