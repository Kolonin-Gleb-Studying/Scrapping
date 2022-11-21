# Сборщик ссылок на изображения для будущего скачивания
from selenium import webdriver
from selenium.webdriver.common.by import By

# Для использования команды curl, т.е. скачивания изображений
import os 
import time

def collect_urls(search_query, photos_count = 10):
    # Отдаётся предпочтение jpeg файлам, но могут попдать и другие расширения
    # При желании можно сформировать поисковый запрос, что будет собирать картинки нужного размера!
    search_query = f'https://yandex.ru/images/search?text={search_query}&itype=jpg&from=tabbar'
    browser = webdriver.Chrome()
    browser.get(search_query)

    # time.sleep(50)

    images_url = []

    # Клик по первому элементу для начала просмотра изображений
    elem = browser.find_element(By.CLASS_NAME, 'serp-item__link')
    elem.click()

    photos_downloaded = 1
    while photos_downloaded != photos_count:
        # Находим элемент класса MMImage-Origin (он у нас один на странице)
        img = browser.find_element(By.CLASS_NAME, "MMImage-Origin")

        # Находим атрибут src
        img_url = img.get_attribute("src")
        print(img_url)

        # Складываем ссылку на изображение в массив
        images_url.append(img_url)
        photos_downloaded += 1

        # Переход к следующему изображению по стрелке
        next = browser.find_element(By.CLASS_NAME, "CircleButton_type_next")
        next.click()

    return images_url

def url_downloader(images_url, user_agent):
    # Установка пользовательского агента curl
    # os.system(f'curl -A {user_agent}')
    # os.system('curl -b cookies.txt ya.ru') # TODO: Для какого url нужно устанавливать cookies? Если я хочу скачать изображения по разным url

    for num, url in enumerate(images_url):
        os.system(f'')
        os.system(f'curl -A "{user_agent}" -b cookies.txt -o {num}.jpg {url}')

images_url = collect_urls('octopuses', 10)

user_agent = ''
with open('user_agent.txt', 'r', encoding='utf-8') as f:
    user_agent = f.readline()

url_downloader(images_url, user_agent)
