# -*- coding: utf-8 -*- #Управление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))


try: 
    # Передаем переменной link ссылку на web - страницу
    link = "http://suninjuly.github.io/redirect_accept.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

    # находим кнгопку button
    button = browser.find_element(By.TAG_NAME, "button")

    # кликаем по button
    button.click()

    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает
    #  массив имён всех вкладок.Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
    new_window = browser.window_handles[1]

    # Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
    # Это делается с помощью команды switch_to.window
    browser.switch_to.window(new_window)

    # Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    # first_window = browser.window_handles[0]

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
