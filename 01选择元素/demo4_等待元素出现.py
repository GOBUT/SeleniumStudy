import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建一个webdriver对象
wd = webdriver.Chrome()
# 隐式等待
wd.implicitly_wait(10)
# 打开网页
wd.get('https://www.byhy.net/_files/stock1.html')
# 找到
element = wd.find_element(By.ID, 'kw')

element.send_keys('通讯\n')

# 如果没找到的话sleep1秒钟，或者是隐式等待
# while True:
#     try:
#         # 返回页面 ID为1 的元素
#         element = wd.find_element(By.ID,'1')
#         # 打印该元素的文字内容
#         print(element.text)
#         break
#     except:
#         time.sleep(1)

element = wd.find_element(By.ID,'1')
# 打印该元素的文字内容
print(element.text)
wd.quit()