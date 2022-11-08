# Парсер новостей с https://lenta.ru/
# 1. Забрать текст новости
# 2. Забрать ссылку на новость
# 3. Забрать время новости

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

# Отправляем драйверу команду на загрузку урла
driver.get("https://lenta.ru/")

# Найдем элемент по имени тега
topnews__columns = driver.find_elements(By.CLASS_NAME, "topnews__column")

for news_column in topnews__columns:
	news = news_column.find_elements(By.TAG_NAME, 'a')

	for n in news:
		# Ссылка на новость
		print(n.get_attribute("href"))
		# Текст новости
		el = n.find_element(By.XPATH, "//span")
		print(el.get_attribute("outherHTML"))

		# Время новости

		# print(n.get_attribute("innerHTML"))

		# print(n.find_element(By.XPATH, "//a or h3").get_attribute("innerHTML"))

