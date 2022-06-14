from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.brainyquote.com/authors/nathan-fielder-quotes')

raw = []

for x in range(1,19):
    a = driver.find_element_by_xpath(f'//*[@id="qpos_1_{x}"]/div[1]/a[1]').text
    raw.append(a)

with open('234fielderquotes.txt', 'a') as f:
    for i in raw:
        f.writelines(i)
