from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建一个webdriver对象
wd = webdriver.Chrome()

# 打开网址
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据class属性选择元素
# xpath中 elements = wd.find_elements(By.XPATH, "//div//p")
# elements = wd.find_elements(By.CLASS_NAME,"animal")
elements = wd.find_elements(By.TAG_NAME,"span")

# 遍历
for element in elements:
    print(element.text)


wd.quit()