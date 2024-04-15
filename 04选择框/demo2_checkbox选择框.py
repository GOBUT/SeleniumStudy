from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 先把已经选择的选择框全部取消勾选
elements = wd.find_elements(By.CSS_SELECTOR,'#s_checkbox input[name="teacher"]:checked')
for element in elements:
    element.click()

# 再点击小雷老师
wd.find_element(By.CSS_SELECTOR,'#s_checkbox input[value="小雷老师"]').click()
element = wd.find_element(By.CSS_SELECTOR,'#s_checkbox input[name="teacher"]:checked')
print("当前选中的是："+element.get_attribute('value'))