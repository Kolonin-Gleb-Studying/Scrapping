# Стандартная библиотека Selenium WebDriver
from selenium import webdriver

# Библиотека для запуска Selenium в режиме невидимки
from selenium_stealth import stealth

# By - класс для указания поиска по различным параметрам
from selenium.webdriver.common.by import By

# Создаем опции для запуска браузера Chrome
options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Создаем окно браузера Firefox под управлением Selenium
driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe', options=options)

stealth(driver,
        #        languages=["en-US", "en"],
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Отправляем драйверу команду на загрузку урла
# driver.get("http://ithub.role.ru/news.html")
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
