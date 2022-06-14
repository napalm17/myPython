from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random as rn

with open('fielderquotes.txt', 'r') as f:
    lines = f.readline().split('. ')
comments = [(i) for i in lines]

driver = webdriver.Chrome('/home/napalm/PycharmProjects/MyProjects/Scraping/chromedriver')
def login(username, password):
    driver.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A112efcdcfa7eb4cb%2C10%3A1608735722%2C16%3Abca4c16334156a16%2Cf383eb9ea268e8c57fa749f1c43c2d9f4b2b9ae73e47daa21b26cd8a03f89147%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22602eb4fc0424417e9e95c20d034042aa%22%7D&response_type=code&flowName=GeneralOAuthFlow')
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
    sleep(2)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
    sleep(2)
    driver.get('https://www.youtube.com/watch?v=r3-Y31ONZuI')
    driver.execute_script("window.scrollTo(0, 600);")
    sleep(2)
    driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer").click()
    driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[1]/button').click()
login("napalmkokusu@gmail.com", "CdjX0woSZvOd0OwF")

def youtube_commenting(comment):
    sleep(1)
    commentbox = '//*[@id="simplebox-placeholder"]'
    driver.find_element_by_xpath(commentbox).click()
    commentbox2 = '//*[@id="contenteditable-root"]'
    driver.find_element_by_xpath(commentbox2).send_keys(comment)
    driver.find_element_by_xpath(commentbox2).send_keys(Keys.CONTROL + Keys.ENTER)

for i in range(10):
    comment = f'"{rn.choice(comments)}."\n- Nathan Fielder'
    youtube_commenting(comment)
