from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.PhantomJS()
    browser.get('http://www.baidu.com/')
    html = browser.page_source
    print(html)
    print('123')
