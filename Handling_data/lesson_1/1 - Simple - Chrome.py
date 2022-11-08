from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем окно браузера Firefox под управлением Selenium
driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')

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
