from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
searchbox.send_keys('Hey You')

seachBut = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
seachBut.click()
