from selenium import webdriver
from selenium.webdriver.common.by import  By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

elements = wd.find_elements(By.CSS_SELECTOR,'[href="http://www.miitbeian.gov.cn"]')

# 选择属性两个部分，a和b,可以用“，”逗号

for element in elements:
    print('-------------')
    print(element.get_attribute('outerHTML'))

wd.quit()