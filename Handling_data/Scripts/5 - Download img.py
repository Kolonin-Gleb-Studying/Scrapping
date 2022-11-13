from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем окно браузера Firefox под управлением Selenium
driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')

# Отправляем драйверу команду на загрузку урла
driver.get("http://ithub.role.ru/download_media.html")

# Найдем элемент по имени тега
img = driver.find_element(By.TAG_NAME, "img")

# Берем аттрибут со ссылкой на картинку
img_src = img.get_attribute("src")
print()
print("Ссылка на картинку:", img_src)
print()

# Сохраняем файл картинки
file = open('Logo.png', 'wb')
file.write(l.screenshot_as_png)
