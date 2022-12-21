from selenium import webdriver

from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

link = "https://lenta.ru/"

driver.get(link)


news = driver.find_elements(By.CLASS_NAME, '_topnews')

counter = 0

print(len(news))

for n in news:

    if counter == 0:
        element = n.find_element(By.TAG_NAME, 'h3') # Получение основного заголовка
        counter = 1
    else:
        element = n.find_element(By.TAG_NAME, 'span')

    print("News title: ", element.get_attribute('innerHTML'))
    print("News link: ", n.get_attribute('href'))

    time_published = n.find_element(By.TAG_NAME,'time')
    time_published = time_published.get_attribute('innerHTML')
    print("News published at: ", time_published)


time.sleep(3)

driver.close()
