from random import randint
import time
import os

# file/ file path manipulation
import configparser

# automate the webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# reddit scrapper that returns a picture
from reddit_scrapper import reddit_scrapper

from helper_functions import scroll_helper, get_random_hashtag

# We need these settings to start instagram in mobile view
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 500, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


class InstagramBot:
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
        time.sleep(1.5)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        # Scroll the login mobile button into view
        # self.driver.execute_script("window.scrollTo(0, 50)")
        scroll_helper(100, self.driver)

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
        time.sleep(1)
        self.driver.get(self.base_url)


    def upload_photo(self, username, password):
        reddit_web_scrapper = reddit_scrapper()
        reddit_web_scrapper.get_image()
        time.sleep(2)
        # Instagram will not allow a send_keys file path unless the svg is clicked first
        upload_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()

        time.sleep(1)
        # Now that the file window has been opened send the image to be uploaded to the input tag
        input_file = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav[2]/div/div/form/input')
        input_file.send_keys(os.getcwd() + '/daily_image/daily.jpg')
        
        time.sleep(2)
        # Once an image is sent to the input instagram prompts the user to save it
        save_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')
        save_button.click()

        time.sleep(1)
        # Get location of caption text area
        text_area = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea')

        # get caption for the photo from description.txt
        with open('./daily_image/description.txt') as f:
            caption = f.readline()

        # Send caption to the text area
        text_area.send_keys(caption)

        # Get final share button
        share_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')

        share_button.click()

        # close window because the file window was opened and selenium can't close it
        time.sleep(1)
        self.restart_igbot(username, password)


    def change_profile_img(self):
        get_photo = reddit_scrapper()
        get_photo.get_image()
        # Send image to instagram profile picture on the hidden input tag
        profile_pic_button = self.driver.find_elements_by_xpath(
            '//*[@id="react-root"]/section/main/section/div[3]/div[1]/div[2]/form/input')[0].send_keys(os.getcwd() + '/daily_image/daily.jpg')

        time.sleep(1)
        save_profile_pic = self.driver.find_elements_by_xpath(
            '//button[contains(text(), "Save")]')[0].click()
        time.sleep(1)
        self.driver.get(base_url)
    

    def restart_igbot(self, username, password):
        self.driver.quit()
        InstagramBot(username, password)


    def like_photo(self):
        like_button = self.driver.find_elements_by_class_name('wpO6b')[0]
        like_button.click()


    def search_hashtag(self):
        hashtag = get_random_hashtag()
        self.driver.get(
            '{}/explore/tags/{}'.format(self.base_url, hashtag))
        time.sleep(2)

        # mimic a scroll
        scroll_helper(510, self.driver)
        time.sleep(1)
        scroll_helper(600, self.driver)
        time.sleep(1)

        # Get a random pic to like
        random_pic = self.driver.find_elements_by_xpath(
            "//a[contains(@href, '/p/')]")[randint(5, 40)]
        self.driver.get(random_pic.get_attribute("href"))

        # Scroll like button into view and click it
        time.sleep(3)
        scroll_helper(500, self.driver)
        self.like_photo()

        # Retrun bot to homepage after clicking like
        time.sleep(0.5)
        self.driver.get(self.base_url)
        





#  if this is the file that is executed when you initially run the program
if __name__ == '__main__':
    config = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config)

    username = cparser['AUTH']['username']
    password = cparser['AUTH']['password']

    ig_bot = InstagramBot(username, password)

    # Wait for page load before clicking this will be changed when bot is running 24/7
    # time.sleep(2)
    # ig_bot.search_hashtag('sage')
    # ig_bot.upload_photo(username, password)





