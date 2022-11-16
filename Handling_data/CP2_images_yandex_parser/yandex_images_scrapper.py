# Примечание - чтобы установить библиотеку pycurl выбрал виртуальное окружение labelimg с python 3.7.13

''' 
Я не уверен, что при парсинге изображений есть необходимость в Selenium
Вероятно, можно обойтись pycurl
'''

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
    get_body = b_obj.getvalue()

    print(get_body)

    '''
    browser = webdriver.Chrome()
    search_url = f"https://yandex.ru/images/search?text={search_query}&from=tabbar"
    images_url = []

    current_ext = ['png', 'jpg', 'jpeg']

    # Открываем браузер с нужной поисковой фразой
    browser.get(search_url)
    elements = browser.find_elements(By.CLASS_NAME, 'rg_i')
    
    count = 0
    for e in elements:
        # Кликаем на каждой картинке
        e.click()
        time.sleep(1)
        element = browser.find_elements(By.CLASS_NAME, 'v4dQwb')

        if count == 0:
            big_img = element[0].find_element(By.CLASS_NAME, 'n3VNCb')
        else:
            big_img = element[1].find_element(By.CLASS_NAME, 'n3VNCb')

        # Находим атрибут src и складываем ссылку на изображение в массив
        url = big_img.get_attribute("src")

        # Получаем расширение файла
        ext = url.split('.')
        if len(ext) < 2:
            continue
        
        ext = ext[-1].lower()
        if ext not in current_ext:
            continue
        
        images_url.append(url)

        # Сохраняем картинку в файл
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/search{count+1}.{ext}", "wb") as file:
                file.write(response.content)

        count += 1

        # Останавливаемся, когда нашли 5 изображений
        if count == 5:
            break
    return images_url
    '''
        

items = search_yandex('Octopuses')
print(items)

