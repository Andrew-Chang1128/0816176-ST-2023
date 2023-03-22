from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def script():
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
    driver.get("https://www.nycu.edu.tw/")
    driver.maximize_window()
    #click on news
    ele = driver.find_element(By.XPATH, "//a[@title='新聞']")
    ele.click()
    #click on the first news
    ele = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div/article/div/div/div/div/section/div/div/div/div/div/div[3]/div/div/div[2]/div[1]/ul/li[1]/a")
    ele.click()
    #print the title of the news
    ele = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/article/header/h1")
    print(f'title: {ele.text}')
    ele = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/article/div")
    print(f'paragraph {ele.text}\n')

    #open tab
    driver.switch_to.new_window('tab')
    driver.get("https://www.google.com")
    ele = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    # /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
    # /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea
    # /html/body/ntp-app//div/div[1]/ntp-realbox//div/input
    ele.send_keys('0816176')
    ele.send_keys(Keys.ENTER)
    #print the title of second result
    ele = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a/h3")
    print(ele.text)
    # /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/a/h3
    # /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/a/h3
    
    # while(1):
    #     pass


if __name__ == "__main__":
    script()
