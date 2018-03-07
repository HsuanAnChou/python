from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
sys.path.append('/Users/apple/Documents/GitHub/python/practice')
import utf8

utf8.setutf8()

searching_word = input("請輸入欲查詢之關鍵字: ")

browser = webdriver.Chrome("/Users/apple/Documents/GitHub/python/chromedriver")
browser.get("https://google.com.tw")
searching_textarea = browser.find_element_by_name('q')
searching_textarea.send_keys("%s\n" %(searching_word))

index = 0
while True:
    index = index + 1
    title_elems = browser.find_elements_by_css_selector("div.srg div.g div div.rc h3.r a")
    content_elems = browser.find_elements_by_css_selector("span.st")
    print("========== page %d ==========" %(index))
    for n in range(0, len(title_elems)):
        print("Titile: %s" %(title_elems[n].text))
        print("Url: %s" %(title_elems[n].get_attribute("href")))
        print("Content:\n\t%s" %(content_elems[n].text))
        print("---")
    sleep(5)
    try:
        next_page = browser.find_element_by_css_selector("#pnnext")
        next_page.click()
    except NoSuchElementException:
        break
print("=============================")
