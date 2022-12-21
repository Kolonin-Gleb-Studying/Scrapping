from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Отправляем драйверу команду на загрузку урла
driver.get("http://ithub.role.ru/download_media.html")

# Скриншот экрана целиком
driver.save_screenshot("screenshot.png")

# Скриншот конкретной области - картинки кота
file = open("cat.png", "wb")
file.write(driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)
file.close()

# Скриншот конкретной области - всего текстового поля
file = open("element.png", "wb")
file.write(driver.find_element(By.CLASS_NAME, 'container').screenshot_as_png)
file.close()
