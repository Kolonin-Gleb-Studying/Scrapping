from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import json

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver=webdriver.Chrome(chrome_options=options)
driver.get("https://www.youtube.com/")

WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys("30 seconds video")

driver.find_element(By.CSS_SELECTOR, "button.style-scope.ytd-searchbox#search-icon-legacy").click()
collected_urls = [my_href.get_attribute("href") for my_href in WebDriverWait(driver, 6).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]

# Чтобы не запускать парсер
# collected_urls = ['https://www.youtube.com/watch?v=BZP1rYjoBgI', 'https://www.youtube.com/watch?v=JzPfMbG1vrE', 'https://www.youtube.com/watch?v=4Kvd-uquuhI', 'https://www.youtube.com/watch?v=RpG7FzXrNSs']

# Оставлю часть видео (5шт)
collected_urls = collected_urls[:5]

# Перехожу к скачиванию видео

# 1) проходитесь по каждой ссылке и извлекаете теги на все доступные варианты видео
for ind, url in enumerate(collected_urls):
    os.system(f"you-get --json {url} > json/{ind}.json")

# 2) находите вариант с самым низким разрешением и форматом mp4
# -- Для этого необходимо распарсить JSON файлы
# Буду считать, что самое низкое разрешение - имеет минимальный size.
# Если size отсутствует, то не участвует в сравнениях.

for file in os.listdir('json'):
    with open(f"json/{file}", 'r', encoding='utf-8') as f:
        json_data = json.load(f) # Результат загрузки - python словарь

        best_option = None # Тут будет номер потока видео, что следует скачать.
        smallest_size = 999999999999999 # Тут вес видео в этом потоке

        for option in json_data['streams'].keys():
            if json_data['streams'][option]["container"] == "mp4":
                try: # Видео, размер которых не известен не участвуют в сравнениях
                    if json_data['streams'][option]["size"] < smallest_size:
                        best_option = option
                        smallest_size = json_data['streams'][option]["size"]
                except KeyError:
                    continue
        # 3) Скачивание ролика выбранного качества
        url = json_data["url"]
        os.system(f"you-get --itag={best_option} {url}")


# Для запуска скрипта открыть command-prompt
# python main2.py
