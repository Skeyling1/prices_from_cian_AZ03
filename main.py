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
prices_elements = driver.find_elements(By.CLASS_NAME, '_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq')

print(prices_elements)

# Извлечение текста цен
prices = [price.text for price in prices_elements]

# Закрываем драйвер
driver.quit()

# Сохранение в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('prices.csv', index=False)

print("Цены успешно сохранены в файл prices.csv")