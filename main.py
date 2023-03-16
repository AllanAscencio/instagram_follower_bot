import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# --------------- CONSTANTS ---------------------- #

CHROME_DRIVER_PATH = "\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "kimberly.loaiza"
USERNAME = "YOURUSERNAME"
PASSWORD = "YOURPASSWORD"


class InstaFollower:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options,
                                       service=Service(executable_path="chromedriver.exe", log_path="NUL"))

    def login_finduser_follow(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        log_in = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        log_in.click()
        log_in.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password.click()
        password.send_keys(PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        login_btn.click()
        time.sleep(4)
        not_now_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div")
        not_now_btn.click()
        not_now2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        not_now2.click()
        self.driver.get("https://www.instagram.com/kimberly.loaiza/")
        time.sleep(4)
        followers_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        followers_btn.click()

        print("Follow start")
        time.sleep(5)

        buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div button")


        for button in buttons:
            button.click()
            print(button.text)
            time.sleep(2)


bot = InstaFollower()
bot.login_finduser_follow()