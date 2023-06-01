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


def StoryView():
    story = driver.find_elements(By.XPATH, "//button//span[@role='link']")
    story[0].click()

    for i in range(len(story)):
        driver.find_element(By.XPATH, "//div[@class=' _9zm2']").click()
        time.sleep(5)

    driver.find_element(By.XPATH, "//div[@class='x78zum5 x6s0dn4 xl56j7k xdt5ytf']//*[name()='svg']").click()
    time.sleep(3)


file = "C:/Users/Vinit/Desktop/New folder/InstaBot.xlsx"

nam = XlSUtility.readdata(file, "Sheet1", 2, 1)
passw = XlSUtility.readdata(file, "Sheet1", 2, 2)

vinit = InstaBot(nam, passw)
vinit.login()

# StoryView()

# driver.find_element(By.XPATH, "//div[contains(text(),'Reels')]").click()
driver.find_element(By.XPATH, "//body//div[2]/div[3]/div[1]/a[1]/div[1]").click()
time.sleep(5)

height = driver.execute_script("return document.body.scrollHeight")
for i in range(1, height, 556):
    driver.execute_script(f"window.scrollTo(0,{i})")
    time.sleep(5)

# height = driver.execute_script("return document.body.scrollHeight")
# for i in range(height):
#     driver.execute_script('window.scrollBy(1, 556)')  # scroll by 556 pixels on each iteration
#     time.sleep(3)
#     # height = driver.execute_script("return document.body.scrollHeight")

# reels = driver.find_elements(By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div/section/main["
#                                        "@role='main']/div/div")
# random_reel = random.choice(reels)
# index = reels.index(random_reel)
# print(len(reels))
# print(index)
#
#
# def ReelScroll():
#     time.sleep(3)
#     act = ActionChains
#     act.move_to_element(reel1).double_click().perform()
#     time.sleep(5)
#
#
# for i in range(len(reels)):
#     if i == 0 or i % 2 == 0:
#         i += 1
#         reel = driver.find_element(By.XPATH, f"//body/div/div/div/div/div/div/div/div/div/div/section/main["
#                                              f"@role='main']/div/div[{i}]")
#         reel1 = driver.find_elements(By.XPATH, f"//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
#                                                f"1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[{i}]/div[1]/div["
#                                                f"1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
#                                                f"1]/div[1]/div[1]/div[2]")
#         ReelScroll()
#     else:
#         reel = driver.find_elements(By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div/section/main["
#                                               f"@role='main']/div/div[{i}]")
#         ReelScroll()

# def Like():
#     time.sleep(5)
#     like_xpath = f"//div[{int(index)}]//div[1]//div[2]//div[1]//span[1]//button[1]//div[2]//span[1]//*[name()='svg']"
#     act = ActionChains(driver)
#     act.move_to_element(like_xpath).click().perform()
#     time.sleep(3)
#
#
# if index == 0 or index % 2 == 0:
#     index = index + 1
#     Like()
# else:
#     Like()

time.sleep(3)

driver.quit()
