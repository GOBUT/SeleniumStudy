from selenium import webdriver
from selenium.webdriver.common.by import  By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")
# 一般的css
# elements = wd.find_elements(By.CSS_SELECTOR,'span')
# css为id时加上#号
# elements = wd.find_elements(By.CSS_SELECTOR,'#searchtext')
# >符号来选择子元素   空格的话就可以跳过中间css选择器
# elements = wd.find_elements(By.CSS_SELECTOR,'#layer1 > span')
elements = wd.find_elements(By.CSS_SELECTOR,'#layer1  span')

for element in elements:
    print(element.get_attribute('outerHTML'))

wd.quit()