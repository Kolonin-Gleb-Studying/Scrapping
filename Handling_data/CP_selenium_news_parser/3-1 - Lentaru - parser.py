# Парсер новостей с https://lenta.ru/

from selenium import webdriver
from selenium.webdriver.common.by import By # By - класс для указания поиска по различным параметрам
import random
import time

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
driver.get("https://lenta.ru/parts/news/")

# Найдем элементы по имени тега
news_list = driver.find_elements(By.CLASS_NAME, "parts-page__item")

links = []
for n in news_list:
    el_a = n.find_element(By.TAG_NAME, "a")
    news_link = el_a.get_attribute("href")
    if "/lenta.ru" in news_link: # Сбор ссылок на новости, что размещены на портале /lenta.ru
        links.append(news_link)  # Чтобы выцеплять текст из всех новостей можно было 1 способом

# Собрали 
print(links)

w = random.randint(1, 4)
print(w)
time.sleep(w)

file = open("news2.txt", "w")
# Перебираем список ссылок и заходим на каждую
for link in links:
    driver.get(link)
    title = driver.find_element(By.XPATH, '//h1/span').get_attribute('innerHTML')

    p_container = driver.find_element(By.CLASS_NAME, 'topic-body__content')
    p_list = p_container.find_elements(By.TAG_NAME, 'p')

    content = ''
    for p in p_list:
        content += p.get_attribute('innerHTML')
        content += "\n"

    print(link + "\n" + title + "\n" + content + "\n")
    file.write(link + "\n" + title + "\n" + content + "\n")

    w = random.randint(3, 10)
    print("Wait read news:", w)
    time.sleep(w)

    driver.back()

    w = random.randint(3, 10)
    print("Wait news list:", w)
    time.sleep(w)

file.close()



