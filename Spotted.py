import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.facebook.com/spottedunicamp2")
time.sleep(1)

# elem = browser.find_element_by_tag_name("body")
# o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q
no_of_pagedowns = 10

# elem = browser.find_element_by_tag_name('body')
elem = browser.find_element_by_class_name('_4vn1')
for i in range(no_of_pagedowns):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# post_elems = browser.find_elements_by_class_name("post-item-title")

# for post in post_elems:
#     print (post.text)
palavras = elem.text.split('\n')
print(palavras)

# palavra = browser.find_element_by_class_name('o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q')
# print(palavra)


