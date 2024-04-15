from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://www.baidu.com/')

from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)

# 鼠标移动到 元素上
ac.move_to_element(
    driver.find_element(By.CSS_SELECTOR, '[name="tj_settingicon"]')
).perform()


# 冻结窗口  setTimeout(function(){debugger}, 5000)
input('')