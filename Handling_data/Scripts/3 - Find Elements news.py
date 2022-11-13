from selenium import webdriver
from selenium.webdriver.common.by import By


# Создаем окно браузера Firefox под управлением Selenium
driver = webdriver.Chrome(executable_path=r'D:\Soft\SeleniumWebDrivers\chromedriver-106.exe')

# Отправляем драйверу команду на загрузку урла
driver.get("http://ithub.role.ru/news.html")

# Найдем элемент по имени тега
#body = driver.find_element(By.TAG_NAME, "body")

print("ВСЕ АБЗАЦЫ")
el_list = driver.find_elements(By.TAG_NAME, 'p')
print(len(el_list))
# Получим текст элемента:
for el_p in el_list:
    outer_html = el_p.get_attribute("outerHTML")
    print(outer_html)


print("")
print("2-Й АБЗАЦ")
body = driver.find_element(By.TAG_NAME, "body")
el_p2 = body.find_element(By.XPATH, "//div[@class='content']/p[2]")
print(el_p2.get_attribute("outerHTML"))


