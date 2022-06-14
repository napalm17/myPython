from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('C:/ProgramData/chocolatey/bin/chromedriver.exe')

def get_questions():
    questions = []
    q = ""
    driver.get('https://www.politicalcompass.org/test')
    for x in range(6):
        for i in range(20):
            try:
                q = driver.find_element_by_xpath(f'/html/body/header/main/article/form/span[{i}]/fieldset/div/legend').text
                driver.find_element_by_xpath(f'/html/body/header/main/article/form/span[{i}]/fieldset/div/div/div/label[4]').click()
                questions.append(q)
            except:
                print("ERROR")
        driver.find_element_by_xpath('/html/body/header/main/article/form/button').click()
    return questions

def create_text(list):
    print(list)
    with open('questions.txt', 'w') as f:
        for i in list:
            f.writelines(i+"\n")

#create_text(get_questions())







