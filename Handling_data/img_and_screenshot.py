from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pyautogui


driver = webdriver.Chrome()
url = "http://ithub.role.ru/download_media.html"
driver.get(url)

# Скриншот экрана целиком
driver.save_screenshot("screenshot.png")

# ActionChains - это низкоуровневый автоматизированный метод взаимодействия, такой как движение мыши,
# работа кнопок мыши, работа с клавишами и взаимодействие с контекстным меню. Это полезно для выполнения
# более сложных операций, таких как наведение и перетаскивание.
action = ActionChains(driver)

# Находим элемент типа img (он у нас один на странице)
img = driver.find_element(By.CSS_SELECTOR, "#agreement > img")

# Выводим меню под правой кнопкой мышки
action.move_to_element(img).context_click().perform()
time.sleep(1)
# Выбираем пункт "Сохранить"
pyautogui.press('down')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)
# Нажимаем кнопку для сохранения изображения (или любого другого файла)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("cat.jpg", interval=0.1) # Сохранение в папку Загрузки
# Нажимаем Enter для сохранения
pyautogui.press('enter')
time.sleep(1)

# Еще раз Enter, если, вдруг, файл уже был
pyautogui.press('enter')
time.sleep(1)
