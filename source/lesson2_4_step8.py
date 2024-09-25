# -*- coding: utf-8 -*- #Управление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))


try: 
    # Передаем переменной link ссылку на web - страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

    # Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться,
    # когда кнопка станет кликабельной. Для реализации подобных ожиданий в Selenium WebDriver 
    # существует понятие явных ожиданий (Explicit Waits), которые позволяют задать специальное
    # ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью 
    # инструментов WebDriverWait
    # говорим Selenium чтобы дождаться стоймости $100 и после этого продолжить действие
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # находим кнгопку button
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn")

    # кликаем по button
    button.click()

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
    button = browser.find_element(By.ID, "solve")

    # кликаем по button
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
