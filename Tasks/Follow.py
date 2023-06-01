import random
import time

import XlSUtility

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

obj = Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.implicitly_wait(10)

driver.get("https://www.instagram.com/")
driver.maximize_window()


# nam = input("Enter UserName: ")
# passw = input("Enter Password: ")


class InstaBot:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self):
        driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.name)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(self.password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        driver.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div["
                                      "1]/div[1]/a[1]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]").click()
        time.sleep(5)


def FollowId():
    driver.find_element(By.XPATH,
                        "//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/a["
                        "1]/div[1]").click()
    time.sleep(2)
    follow = input("Enter Insta Id - ")
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(follow)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//a[@href='/{follow}/']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//header//section/div/div/div/div/button").click()
    time.sleep(5)


file = "C:/Users/Vinit/Desktop/New folder/InstaBot.xlsx"

nam = XlSUtility.readdata(file, "Sheet1", 2, 1)
passw = XlSUtility.readdata(file, "Sheet1", 2, 2)

vinit = InstaBot(nam, passw)
vinit.login()
FollowId()
