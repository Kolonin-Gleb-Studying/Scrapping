# Сборщик ссылок на изображения для будущего скачивания

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# import time

# import pyautogui

def collect_urls(search_query, photos_count = 10):
    # extensions = ['png', 'jpg', 'jpeg']

    # Отдаётся предпочтение jpeg файлам, но могут попдать и другие расширения
    # При желании можно сформировать поисковый запрос, что будет собирать картинки нужного размера!
    search_query = f'https://yandex.ru/images/search?text={search_query}&itype=jpg&from=tabbar'
    browser = webdriver.Chrome()
    browser.get(search_query)

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
        """
        if not img_url.split('.')[-1] in extensions:
            continue
        """
        # ActionChains - это низкоуровневый автоматизированный метод взаимодействия, такой как движение мыши,
        # работа кнопок мыши, работа с клавишами и взаимодействие с контекстным меню. Это полезно для выполнения
        # более сложных операций, таких как наведение и перетаскивание.
        """
        action = ActionChains(browser)
        
        # Выводим меню под правой кнопкой мышки
        action.move_to_element(elem).context_click().perform()
        # Выбор команды сохранить
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')

        # Установка названия файла
        # filename = f"octopus_{photos_downloaded}.{img_url.split('.')[-1]}"
        # pyautogui.write(filename)
        pyautogui.press('enter')

        # Еще раз Enter, если, вдруг, файл уже был
        pyautogui.press('enter')
        """

        # Складываем ссылку на изображение в массив
        images_url.append(img_url)
        photos_downloaded += 1

        # elem.click()
        # elem = browser.find_element(By.CLASS_NAME, 'serp-item__link')

        # Переход к следующему изображению по стрелке
        next = browser.find_element(By.CLASS_NAME, "CircleButton_type_next")
        next.click()

    return images_url

images_url = collect_urls('octopuses', 30)
# print("Ссылки на изображения:", images_url)

with open('octopuses_links.txt', 'w', encoding='utf-8') as file:
    for url in images_url:
        file.write("%s\n" % url)

