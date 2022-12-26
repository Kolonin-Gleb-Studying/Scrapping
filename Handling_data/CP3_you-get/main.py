from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import json

"""
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver=webdriver.Chrome(chrome_options=options)
driver.get("https://www.youtube.com/")

WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys("30 seconds video")

driver.find_element(By.CSS_SELECTOR, "button.style-scope.ytd-searchbox#search-icon-legacy").click()
collected_urls = [my_href.get_attribute("href") for my_href in WebDriverWait(driver, 6).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]
"""

# Чтобы не запускать парсер
collected_urls = ['https://www.youtube.com/watch?v=BZP1rYjoBgI', 'https://www.youtube.com/watch?v=JzPfMbG1vrE', 'https://www.youtube.com/watch?v=4Kvd-uquuhI', 'https://www.youtube.com/watch?v=RpG7FzXrNSs']

# Оставлю часть видео
collected_urls = collected_urls[:6]

# Перехожу к скачиванию видео

# 1) проходитесь по каждой ссылке и извлекаете теги на все доступные варианты видео


for url in collected_urls:
    jsonString = json.dumps(os.system(f"you-get --json {url}"))

    with open('data.json', 'w') as f:
        json.dump(jsonString, f)
    break

# 2) находите вариант с самым низким разрешением и форматом mp4


# 3) загружаете ролик с помощью You-Get на диск использовав нужный тег


# Для запуска скрипта python main.py


# 