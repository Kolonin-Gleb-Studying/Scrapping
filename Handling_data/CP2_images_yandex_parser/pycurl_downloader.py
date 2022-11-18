# Примечание - чтобы установить библиотеку pycurl выбрал виртуальное окружение labelimg с python 3.7.13

# Не работает (60, 'SSL certificate problem: unable to get local issuer certificate')
'''

# Библиотека для использования команды cURL из Python
# Позволит скачать изображения в файлы по подготовленным ссылкам
import pycurl 


import pickle # Для загрузки подготовленного cookies файла
from io import BytesIO # Библиотека для работы с байтовыми последовательностями

# Может пригодиться:
import time
import requests
# import pyautogui

def download(img_url):
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
    crl.setopt(crl.URL, img_url) #ya.ru

    # Устанавливаем объект, в который будет направлен поток данных, который вернет сервер
    crl.setopt(crl.WRITEDATA, b_obj)

    print(img_url)
    # Выполняем запрос
    crl.perform()

    # Закрываем соединение
    crl.close()

    # Получаем содержимое в виде строки
    get_body = b_obj.getvalue().decode('utf8')
    print(get_body)



with open('links.txt', 'r', encoding="utf-8") as file:
    for line in file.readlines():
        download(line.rstrip())
        break

'''
