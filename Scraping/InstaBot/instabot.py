from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
class InstaBot:
    driver = webdriver.Chrome('C:/Users/CanBerkay/Documents/Coding/Python/Projects/My projects/chromedriver.exe')
    def __init__(self, username, pw):
        self.driver.get('https://instagram.com')
        self.username = username
        self.pw = pw
    def login(self):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.pw)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
    def nathan(self):
        sleep(3)
        self.driver.get('https://www.instagram.com/nathanfielder/')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a').click()
        while True:
            try:
                sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').send_keys(Keys.ARROW_RIGHT)
            except:
                print("DONE")
                break


def control():
    Ins_Bot = InstaBot("thomasbrook17", "Darkknight17")
    Ins_Bot.login()
    Ins_Bot.nathan()

control()