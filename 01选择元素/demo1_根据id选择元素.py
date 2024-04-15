from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个webdriver对象
# wd = webdriver.Chrome(service=Service(r'/Volumes/code/ChromeDriver/chrome-mac-x64/Google Chrome for Testing.app'))
wd = webdriver.Chrome()
# 打开百度
wd.get('https://www.byhy.net/_files/stock1.html')

# 根据id选择元素
element = wd.find_element(By.ID,'kw')

# 输入字符
element.send_keys('航空')

# 查询按钮
element = wd.find_element(By.ID,'go')
element.click()

wd.quit()