# -*- coding: utf-8 -*- #”правление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

# функци€ calc
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    # ѕередаем переменной link ссылку на web - страницу
    link = "https://suninjuly.github.io/math.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

    # находим элемент и инциализируем x_element
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    # инициализируем значением функции calc значение y
    y = calc(x)
   
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

    # функци€ задержки времени
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождени€ скрипта
    time.sleep(10)
    # закрываем браузер после всех манипул€ций
    browser.quit()
