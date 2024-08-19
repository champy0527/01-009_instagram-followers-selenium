from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
import time

load_dotenv()

# -------------------------- CONSTANTS --------------------------#

SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")
THRESHOLD = 10  # The amount of accounts I want to follow so I don't get detected as a bot


# ---------------------------- BODY ----------------------------#

class InstagramBot:
    URL = "https://www.instagram.com"

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(1)
        self.wait = WebDriverWait(self.driver, 10)

    def login_to_ig(self):
        self.driver.get(self.URL)

        time.sleep(3)

        # TODO Decline Optional Cookies
        try:
            decline_cookies = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Decline optional cookies']")))
            time.sleep(1)
            decline_cookies.click()
        except Exception as e:
            print(f"Failed to decline optional cookies: {e}")

        # TODO Enter username
        try:
            username = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
            time.sleep(1)
            username.send_keys(IG_USERNAME, Keys.TAB)
        except Exception as e:
            print(f"Failed to enter username: {e}")

        # TODO Enter password slowly
        try:
            password = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
            time.sleep(1)
            for letter in IG_PASSWORD:
                password.send_keys(letter)
                time.sleep(0.5)
            password.send_keys(Keys.ENTER)

        except Exception as e:
            print(f"Failed to enter password: {e}")

        # TODO Decline Notification Prompt
        try:
            no_notification = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Not Now']")))
            time.sleep(3)
            no_notification.click()
        except Exception as e:
            print(f"Failed to decline notification prompt: {e}")

    def find_followers(self):
        # TODO Search Similar Account
        try:
            url_followers = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
            self.driver.get(url_followers)
            time.sleep(3)
        except Exception as e:
            print(f"Failed to search similar account: {e}")

        # TODO Click on Followers
        try:
            followers = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/shihtzuclubs/followers/']")))
            time.sleep(1)
            followers.click()
        except Exception as e:
            print(f"Failed to open followers page: {e}")

    def follow(self):
        # TODO follow followers up to THRESHOLD
        try:
            buttons = self.driver.find_elements(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-._ap30")

            i = 0
            followed_accounts_count = 0
            while followed_accounts_count < THRESHOLD:
                if buttons[i].text == "Following":  # If I'm already following this account
                    i += 1  # skip this button's index
                    continue
                buttons[i].click()
                time.sleep(1.5)
                followed_accounts_count += 1  # Only count the followed accounts. This makes sure I only follow X amount
                i += 1

        except Exception as e:
            print(f"Follow button has already been clicked: {e}")

    def close_driver(self):
        time.sleep(10)
        self.driver.quit()


instagram_bot = InstagramBot()
instagram_bot.login_to_ig()
instagram_bot.find_followers()
instagram_bot.follow()
instagram_bot.close_driver()
