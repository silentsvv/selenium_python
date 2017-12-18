from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # browser = webdriver.Chrome()
    browser = webdriver.PhantomJS()
    browser.get('http://www.baidu.com/')
    search = browser.find_element(by='id', value='kw')
    search.send_keys('vue'+ Keys.RETURN)
    try:
        element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'result'))
        WebDriverWait(browser, 5).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    result = browser.get_screenshot_as_file('./ScreenShot/test2.png')
    newResult = browser.page_source
    soup = BeautifulSoup(newResult, 'html.parser').get_text()
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(soup)
