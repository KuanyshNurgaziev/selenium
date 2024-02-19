from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Создаем новый экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Переходим на страницу Google
driver.get("https://www.google.com")
time.sleep(5)

# Находим заголовок страницы
title = driver.title
print(title)

# Закрываем браузер после теста
driver.quit()
