# -*- coding: utf-8 -*- #Управление кодировкой UTF-8
# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Передаем переменной link ссылку на web - страницу
    link = "https://suninjuly.github.io/selects1.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

    # Нахождение элемента по id
    element = browser.find_element(By.ID, 'num1') 
    element2 = browser.find_element(By.ID, 'num2') 

    # Считываем элементы c помощью(.text) и складываем приводя к типу int
    y = int(element.text) + int(element2.text)

    # находим окно для ввода результата
    input1 = browser.find_element(By.CSS_SELECTOR, '#dropdown')
    # Вставляем результат в окно
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()