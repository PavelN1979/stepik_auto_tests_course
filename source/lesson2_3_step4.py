# -*- coding: utf-8 -*- #Управление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))


try: 
    # Передаем переменной link ссылку на web - страницу
    link = "https://suninjuly.github.io/alert_accept.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

    # находим кнгопку button
    button = browser.find_element(By.TAG_NAME, "button")

    # кликаем по button
    button.click()

    # вариант модального окна, который предлагает пользователю выбор согласиться
    # с сообщением или отказаться от него, называется confirm.
    confirm = browser.switch_to.alert
    confirm.accept()

    # находим элемент и инциализируем x_element
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text

    # инициализируем значением функции calc значение y
    y = fanc(int(x))
    
    # находим окно для ввода результата
    input = browser.find_element(By.CSS_SELECTOR, '#answer')

    # Вставляем результат в окно
    input.send_keys(y)

    # находим кнгопку button
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn")

    # кликаем по button
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
