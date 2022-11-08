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

# Парсинг новостей про спорт
driver.get("https://sport24.ru/")



# Найдем элементы, содержащие списки новостей
all_links = driver.find_elements(By.TAG_NAME, 'a')

# Проверить ссылку на наличие /news



news_links = []

for link in all_links:
    if "https://sport24.ru/news/" in link.get_attribute("href"):
        news_links.append(link.get_attribute("href"))

# Возьму первые 10 новостей
news_links = news_links[:10]

# Открываю каждую ссылку новости и читаю из неё информацию

with open('sport_news.txt', "a", encoding='utf-8') as f:
    for link in news_links:
        driver.get(link)
        p_list = driver.find_elements(By.TAG_NAME, 'p')

        content = ''
        for p in p_list:
            content += p.text
            content += "\n"
        f.write(content + "\n")
        # print(content)
    # print(news_links)
