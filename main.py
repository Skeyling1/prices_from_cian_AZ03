from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

url = 'https://syktyvkar.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver = webdriver.Chrome()

# Открываем страницу
driver.get(url)

# Даем время на загрузку страницы
time.sleep(5)

# Поиск элементов с ценами
prices_elements = driver.find_elements(By.XPATH, '//span[@data-mark="MainPrice"]/span')

print(prices_elements)

# Извлечение текста цен
prices = [price.text for price in prices_elements]

# Закрываем драйвер
driver.quit()

# Сохранение в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('prices.csv', index=False)

print("Цены успешно сохранены в файл prices.csv")