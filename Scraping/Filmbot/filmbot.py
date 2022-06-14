from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('C:/ProgramData/chocolatey/bin/chromedriver.exe')
def get_film(username, password):
    watchlist = []
    film_title = ""
    year = ""
    driver.get('https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS91c2VyL3VyNzA2OTAwNTYvd2F0Y2hsaXN0P3JlZl89bG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20')
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    driver.find_element_by_xpath('//*[@id="center-1-react"]/div/div[3]/div[2]/button').click()
    driver.execute_script("window.scrollTo(500, 18000);")
    for i in range(2, 120):
        try:
            film_title = driver.find_element_by_xpath(f'//*[@id="center-1-react"]/div/div[3]/div[1]/div[{i}]/div/div[2]/h3').text
            year = driver.find_element_by_xpath(f'//*[@id="center-1-react"]/div/div[3]/div/div[{i}]/div/div[2]/p[1]/span[1]').text
            watchlist.append("{}-{}".format(film_title, year))
        except:
            watchlist.append("UNSUCCESFUL")
        if film_title == "Lethal Weapon 2":
            break
    return watchlist

def create_text(list):
    print(list)
    with open('watchlist_final.txt', 'w') as f:
        for i in list:
            f.writelines(i + "\n")

#create_text(get_film('suerberkay17@gmail.com', 'qF9HcnlDmWkrlbWN'))
