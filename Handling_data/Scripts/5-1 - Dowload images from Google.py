from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

def search_google(search_query):
    browser = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
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


# Ищем котиков
items = search_google('cats')
print(items)
