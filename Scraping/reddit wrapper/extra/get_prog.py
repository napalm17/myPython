from selenium import webdriver

#driver = webdriver.Chrome('C:/ProgramData/chocolatey/bin/chromedriver.exe')
artists = []

def get_artists():
    driver.get('https://www.ranker.com/crowdranked-list/most-beautiful-celebrities')
    for i in range(0, 250):
        print(i)
        try:
            item = driver.find_element_by_xpath(f'/html/body/div[1]/article/div[2]/div/ul/li[{i}]/div[2]/div/h2/a').text
            artists.append(item)
            print(item)
        except:
            artists.append("ERROR")

def write_text():
    with open('celebs.txt', 'r') as f:
        l = f.read().split('\n')
        for i in l:
            if i =="ERROR":
                l.remove(i)
        print(l)
    with open('celebs.txt', 'w') as f:
        for x in l:
            f.write(x + "\n")
#get_artists()
#write_text()