from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pyautogui


img_logo = r'D:\My Documents\IT hub\GD - get-grab data\selenium\hey-google-logo.png'


driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')
url = "https://www.google.com"
driver.get(url)

# Ищем ссылку на изображение
logo_url = driver.find_element(By.CLASS_NAME, "lnXdpd").get_attribute("src")

# Переходим на страницу, где откроется только логотип
driver.get(logo_url)

# ActionChains - это низкоуровневый автоматизированный метод взаимодействия, такой как движение мыши,
# работа кнопок мыши, работа с клавишами и взаимодействие с контекстным меню. Это полезно для выполнения
# более сложных операций, таких как наведение и перетаскивание.
action = ActionChains(driver)

# Находим элемент типа img (он у нас один на странице)
img = driver.find_element(By.XPATH, "//img")

# Выводим меню под правой кнопкой мышки
action.move_to_element(img).context_click().perform()
time.sleep(1)
# Выбираем пункт "Сохранить"
# pyautogui.hotkey('command', 's') - если бы Google не убрал бы горячие клавиши
pyautogui.press('down')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)

# Нажимаем кнопку для сохранения изображения (или любого другого файла)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(img_logo, interval=0.1)

# Нажимаем Enter для сохранения
pyautogui.press('enter')
time.sleep(1)

# Еще раз Enter, если, вдруг, файл уже был
pyautogui.press('enter')
time.sleep(1)
