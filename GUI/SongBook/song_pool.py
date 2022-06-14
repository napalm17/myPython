from time import sleep
from selenium import webdriver


def get_song(username, pw):
    driver = webdriver.Chrome('C:/ProgramData/chocolatey/bin/chromedriver.exe')
    list = []
    driver.get('https://www.statsforspotify.com/track/top')
    driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="login-button"]').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="auth-accept"]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/ul/li[2]/a').click()
    sleep(2)
    for i in range(1, 70):
        try:
            song = driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/div/table/tr[{i}]/td[5]').text
            artist = driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/div/table/tr[{i}]/td[6]').text
            list.append("{}--{}".format(song, artist))
        except:
            print("AAAAAAA")
    return list





def create_text(list):
    print(list)
    with open('songlist.txt', 'w') as f:
        for i in list:
            f.writelines(i + "\n")

#create_text(get_song("berkaysuer.17@gmail.com", "3hZtfuPKjxXl95vu"))