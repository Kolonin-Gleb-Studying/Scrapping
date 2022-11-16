# Код для авторизации на GitHub
# https://github.com/login

import time

from selenium import webdriver
from selenium.webdriver.common.by import By # By - класс для указания поиска по различным параметрам

# Библиотека для запуска Selenium в режиме невидимки
from selenium_stealth import stealth

# Создаем опции для запуска браузера Chrome
options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Создаем окно браузера Firefox под управлением Selenium
# executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe',
driver = webdriver.Chrome(options=options)

stealth(driver,
        # languages=["en-US", "en"],
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Github логин и пароль для входа
username = "************"
password = "*********"

# Открытие страницы
driver.get("https://github.com/login")

# Отправка логина
driver.find_element(By.ID, "login_field").send_keys(username)
# Отправка пароля
driver.find_element(By.ID, "password").send_keys(password)
# Клик по кнопке входа
driver.find_element(By.NAME, "commit").click()

time.sleep(4) # Чтобы увидеть результат