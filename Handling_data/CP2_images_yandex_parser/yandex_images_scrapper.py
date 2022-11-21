# Примечание - чтобы установить библиотеку pycurl выбрал виртуальное окружение labelimg с python 3.7.13

# Не работает. Отдаёт Captcha
"""
# Для парсинга
# Нахождение изображений и взятия их ссылок
from selenium import webdriver
from selenium.webdriver.common.by import By

# Библиотека для использования команды cURL из Python
# Позволит скачать изображения в файлы по подготовленным ссылкам
import pycurl 


import pickle # Для загрузки подготовленного cookies файла
from io import BytesIO # Библиотека для работы с байтовыми последовательностями

# Может пригодиться:
import time
import requests
# import pyautogui

def search_yandex(search_query):
    # Создаем объект для приема данных в формате последовательности байтов
    b_obj = BytesIO()

    # Создаем объект Curl
    crl = pycurl.Curl()
    
    # Подстановка cookies в pycurl:
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print(type(cookies))

    crl.setopt(pycurl.COOKIELIST, str(cookies))

    # Подстановка имени браузера в pycurl:
    user_agent = ""
    with open('user_agent.txt', 'r', encoding='utf-8') as f:
        user_agent = f.readline()

    crl.setopt(pycurl.USERAGENT, user_agent)

    # Устанавливаем опцию источника
    search_query = f'yandex.ru/images/search?text={search_query}&from=tabbar'
    crl.setopt(crl.URL, search_query)

    crl.setopt(crl.FOLLOWLOCATION, True)

    # Устанавливаем объект, в который будет направлен поток данных, который вернет сервер
    crl.setopt(crl.WRITEDATA, b_obj)

    # Выполняем запрос
    crl.perform()
    
    # Получаем содержимое в виде строки
    get_body = b_obj.getvalue().decode('utf8')

    print(get_body)
    return 1

items = search_yandex('Octopuses')
print(items)
"""
