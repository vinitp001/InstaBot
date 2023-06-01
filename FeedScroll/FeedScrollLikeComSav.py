import random
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

obj = Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=obj, options=ops)
driver.implicitly_wait(10)

driver.get("https://www.instagram.com/")
driver.maximize_window()

nam = input("Enter UserName: ")
passw = input("Enter Password: ")


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

        time.sleep(2)

        try:
            driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]").click()
        except NoSuchElementException:
            print("No such element")
        time.sleep(5)


def FeedScroll():
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    for i in range(1, height, 312):
        driver.execute_script(f'window.scrollTo(0, {i})')
        time.sleep(3)

    time.sleep(2)
    driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")


def LikeSaveComment():
    like_xpath = f"//article[{int(index)}]//div[1]//div[3]//div[1]//div[1]//section[1]//span[1]//button[1]"
    driver.find_element(By.XPATH, like_xpath).click()
    time.sleep(3)
    save_xpath = f"//article[{int(index)}]//div[1]//div[3]//div[1]//div[1]//section[1]//span[4]//div[1]//div[" \
                 f"1]//button[1] "
    driver.find_element(By.XPATH, save_xpath).click()
    time.sleep(5)

    comment_xpath = f"//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[" \
                    f"1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/article[{int(index)}]/div[1]/div[" \
                    f"3]/div[1]/div[1]/section[3]/div[1]/form[1]/div[1]/textarea[1]"
    driver.find_element(By.XPATH, comment_xpath).send_keys(input("Comment = "))

    act = ActionChains(driver)
    act.send_keys(Keys.ENTER).perform()

    time.sleep(3)


insta = InstaBot(nam, passw)
insta.login()
FeedScroll()
time.sleep(5)

articles = driver.find_elements(By.XPATH, "//article")
random_article = random.choice(articles)
index = articles.index(random_article)
print(index)

if index == 0:
    index = index + 1
    LikeSaveComment()
else:
    LikeSaveComment()

time.sleep(3)

driver.quit()

# act.double_click(random_article).perform()
# time.sleep(3)
