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
# ,executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe',
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

# Парсинг новостей про технологии
driver.get("https://www.techcult.ru/technology")

# Найдем элементы, содержащие списки новостей
news_block = driver.find_element(By.ID, "content_col")
news_links = news_block.find_elements(By.CLASS_NAME, "pad")

# print(len(news_links))
# Возьму первые 10 новостей
news_links = news_links[:10]


# Открываю каждую ссылку новости и читаю из неё информацию
with open('tech_news.txt', "a", encoding='utf-8') as f:
    for link in news_links:
        print(link.get_attribute("href"))
        driver.get(link.get_attribute("href"))
        
        p_list = driver.find_elements(By.TAG_NAME, 'p')

        content = ''
        for p in p_list:
            content += p.text
            content += "\n"
        f.write(content + "\n")
        # print(content)
        # print(news_links)


