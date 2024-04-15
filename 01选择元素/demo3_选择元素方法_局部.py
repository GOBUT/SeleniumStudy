
from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建一个webdriver对象
wd = webdriver.Chrome()

# 打开网址
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据class属性选择元素
element = wd.find_element(By.ID,"container")

# 限制选择元素的范围是id为container元素的内部
spans = element.find_elements(By.TAG_NAME,'span')
for span in spans:
    print(span.text)


wd.quit()