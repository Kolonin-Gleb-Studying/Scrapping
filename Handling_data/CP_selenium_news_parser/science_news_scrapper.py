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

# Парсинг новостей по науке 
# driver.get("https://new-science.ru/")

# Парсинг новостей по космонавтике
driver.get("https://new-science.ru/category/kosmonavtika/")


# news_block = driver.find_element(By.CLASS_NAME, "container-wrapper")
news_block = driver.find_element(By.CLASS_NAME, "wide-post-box")

# Найдем элементы, содержащие списки новостей
post_titles = news_block.find_elements(By.CLASS_NAME, "post-title")

news_links = []

for pt in post_titles:
    raw = pt.get_attribute("innerHTML")
    news_links.append(raw[raw.find('\"')+1:raw.find('\"', 10)-1])
    
# print(len(news_links))
# print(news_links)

# Открываю каждую ссылку новости и читаю из неё информацию
# with open('science_news.txt', "a", encoding='utf-8') as f:
with open('space_news.txt', "a", encoding='utf-8') as f:
    for link in news_links:
        driver.get(link)

        p_list = driver.find_elements(By.TAG_NAME, 'p') # Что если внутри картинка

        content = ''
        for p in p_list:
            content += p.text
            content += "\n"
        f.write(content + "\n")

