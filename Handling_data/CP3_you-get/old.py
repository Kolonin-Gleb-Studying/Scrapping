# Сборщик ссылок на изображения для будущего скачивания
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Для использования графического интерфейса ОС при ПКМ
# import pycurl

import os # Для использования команды curl, т.е. скачивания изображений
import time

def collect_urls(videos_count = 5):
    # Поисковый запрос для нахождения коротких видео (30 - 60 секунд)
    search_query = f'https://www.youtube.com/results?search_query=30+seconds+video'
    browser = webdriver.Chrome()
    browser.get(search_query)

    # Жду загрузки сайта
    time.sleep(5)

    el = browser.find_element(By.TAG_NAME, 'html')

    print(el.get_attribute("outerHTML"))

    videos_url = []

    

    # Взять ссылки на видео из эллементов на сайте

    # Клик по первому элементу для начала просмотра изображений
    elements = browser.find_elements(By.TAG_NAME, 'a')

    for el in elements:
        if "https://www.youtube.com/watch?" in el.get_attribute("href"):
            videos_url.append(el.get_attribute("href"))
            if len(videos_url) == 5:
                break # Больше не нужно собирать видео

    print(videos_url)

    return None

    photos_downloaded = 1
    while photos_downloaded != videos_count:
        # Находим элемент класса MMImage-Origin (он у нас один на странице)
        img = browser.find_element(By.CLASS_NAME, "MMImage-Origin")

        # Чтобы в src появился путь к изображений в полном масштабе необходимо кликнуть на него ПКМ

        # ActionChains - это низкоуровневый автоматизированный метод взаимодействия, такой как движение мыши,
        # работа кнопок мыши, работа с клавишами и взаимодействие с контекстным меню. Это полезно для выполнения
        # более сложных операций, таких как наведение и перетаскивание.
        action = ActionChains(browser)

        # Выводим меню под правой кнопкой мышки
        action.move_to_element(img).context_click().perform()

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


def url_downloader(images_url):
    # Скачать видео используя собранные ссылки и you-get
    pass

images_url = collect_urls(videos_count=5)


# url_downloader(images_url)


# Попробую сначала просто скачать 1 видео по запросу себе на пк
# Могу вписать команду в модуль os

"""
Загрузка конкретного ролика:
you-get https://youtu.be/YEpU27W2ZAw

Посмотреть список разрешений для видеоролика:
you-get -i https://youtu.be/YEpU27W2ZAw

Скачать ролик только нужного качества:
you-get --tag=278 https://youtu.be/YEpU27W2ZAw

"""
