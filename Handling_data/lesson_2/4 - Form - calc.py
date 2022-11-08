from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Создаем окно браузера Firefox под управлением Selenium
driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')

# Отправляем драйверу команду на загрузку урла
driver.get("http://ithub.role.ru/calc.php")

# Ищем элемент input
inp = driver.find_element(By.TAG_NAME, 'input')
# Ищем кнопку
but = driver.find_element(By.XPATH, "//form/p/button[@value='calc']")

inp.send_keys('9')
time.sleep(3)
but.click()

time.sleep(3)

rez = driver.find_element(By.TAG_NAME, 'b')
print("")
print(rez.get_attribute("outerHTML"))


