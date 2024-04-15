from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()

# 先保存当前浏览器窗口的句柄
mainWindow = wd.current_window_handle


# 获取浏览器句柄
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if 'Bing' in wd.title:
        break
# wd.title属性是当前窗口的标题栏 文本
print(wd.title)

wd.find_element(By.ID,'sb_form_q').send_keys('gobut')

# 切换回主窗口
wd.switch_to.window(mainWindow)

wd.find_element(By.ID,'outerbutton').click()

input('')
