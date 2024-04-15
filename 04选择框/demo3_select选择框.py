from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

select = Select(wd.find_element(By.ID,'ss_single'))

# 通过select对象选中小雷老师
select.select_by_visible_text("小雷老师")

wd.quit()

