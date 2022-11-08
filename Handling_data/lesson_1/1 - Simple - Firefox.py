from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Создаем окно браузера Firefox под управлением Selenium
firefox_path = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(executable_path=r'D:\Soft\SeleniumWebDrivers\geckodriver.exe', firefox_binary=firefox_path)

# Отправляем драйверу команду на загрузку урла
driver.get("http://ithub.role.ru/news.html")

# Найдем элемент по имени тега
body = driver.find_element(By.TAG_NAME, "body")

# Попробуем вывести элемент
print(body)

# Получим текст элемента:
inner_html = body.get_attribute("innerHTML")
outer_html = body.get_attribute("outerHTML")

print(inner_html)
print("\n===============================\n")
print(outer_html)


