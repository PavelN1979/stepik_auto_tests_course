# -*- coding: utf-8 -*- #Управление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

# функция calc
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    # Передаем переменной link ссылку на web - страницу
    link = "http://suninjuly.github.io/get_attribute.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()
    # открываем в браузере web - страницу
    browser.get(link)

    # Нахождение элемента по id
    element = browser.find_element(By.ID, 'treasure') 

    # Получение значения атрибута с помощью функции get_attribute()
    x_element = element.get_attribute('valuex')
    
    # инициализируем значением функции calc значение y
    y = calc(x_element)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    # находим кнопку checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")

    # кликаем по checkbox
    option1.click()

    # находим кнопку radiobutton
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")

    # кликаем по radiobutton
    option2.click()

    # находим кнгопку button
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # кликаем по button
    button.click()

    # функция задержки времени
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
