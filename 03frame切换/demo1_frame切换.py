from selenium import webdriver
from selenium.webdriver.common.by import  By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://cdn2.byhy.net/files/selenium/sample2.html")

# 切换到内层frame
wd.switch_to.frame('frame1')
elements = wd.find_elements(By.CSS_SELECTOR,'.plant')

# 选择属性两个部分，a和b,可以用“，”逗号

for element in elements:
    print('-------------')
    print(element.get_attribute('outerHTML'))

# 切换到外层frame
wd.switch_to.default_content()
wd.find_element(By.ID,'outerbutton').click()
wd.quit()