from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем окно браузера Firefox под управлением Selenium
driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')

# Отправляем драйверу команду на загрузку урла
#driver.get("http://ithub.role.ru/news.html")
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
