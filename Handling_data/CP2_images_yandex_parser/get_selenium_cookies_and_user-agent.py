import pickle
from selenium import webdriver

# Получение cookie файла для определенного поискового запроса
# В pickle файл
'''
search_query = 'octopuses'

browser = webdriver.Chrome()
search_url = f"https://yandex.ru/images/search?text={search_query}&from=tabbar"

browser.get(search_url)
pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
'''

# Получение cookie файла для определенного поискового запроса
# В txt файл
'''
search_query = 'octopuses'

browser = webdriver.Chrome()
search_url = f"https://yandex.ru/images/search?text={search_query}&from=tabbar"

browser.get(search_url)

with open('cookies.txt', 'w', encoding='utf-8') as f:
    f.write(str(browser.get_cookies()))
'''

# Загрузка cookie файла
# В python объект
''''''
cookies = pickle.load(open("cookies.pkl", "rb"))
print(cookies)
print(type(cookies))
# print(str(cookies)) # - для передачи в функцию

# Получение user agent в txt файл
'''
browser = webdriver.Chrome()

user_agent = browser.execute_script("return navigator.userAgent;")

with open('user_agent.txt', 'w', encoding='utf-8') as f:
    f.write(user_agent)
'''

# Чтение user agent из txt файла
'''
user_agent = ""

with open('user_agent.txt', 'r', encoding='utf-8') as f:
    user_agent = f.readline()

print(user_agent)
'''
