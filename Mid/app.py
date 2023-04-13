from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


def script():
    
    options = Options()

    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
    driver.get("https://docs.python.org/3/tutorial/index.html")
    driver.maximize_window()
    select = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@class='switchers']/div[1]/select[@id='language_select']"))))
    select.select_by_visible_text('Traditional Chinese')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[@lang='zh_TW']")))
    print(driver.find_elements(By.XPATH, "//section[@id='the-python-tutorial']/h1")[0].text)
    print(driver.find_elements(By.XPATH, "//section[@id='the-python-tutorial']/p")[0].text)


    search = driver.find_element(By.XPATH, "//div[@class='inline-search']/form[@class='inline-search']/input[@name='q']")
    search.send_keys('class')
    search.send_keys(Keys.ENTER)

    for i in range(1,6):
        searchStr =  "//div[@id='search-results']/ul[@class='search']/li[" + str(i) + "]/a"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, searchStr)))
        print(element.text) 
    # while(1):
    #     pass


if __name__ == "__main__":
    script()
