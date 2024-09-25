# -*- coding: utf-8 -*- #Управление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

    # находим элемент и инциализируем x_element
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text

    # инициализируем значением функции calc значение y
    y = fanc(int(x))

    # находим окно для ввода результата
    input = browser.find_element(By.CSS_SELECTOR, '#answer')

    # Вставляем результат в окно
    input.send_keys(y)

    # находим кнопку checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")

    # кликаем по checkbox
    option1.click()

     # метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
    browser.execute_script("window.scrollBy(0, 100);")

    # находим кнопку radiobutton
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")

    # кликаем по radiobutton
    option2.click()
    
    # находим кнгопку button
    button = browser.find_element(By.TAG_NAME, "button")

    #browser.execute_script("return arguments[0].scrollIntoView(true);", button):
    # Этот код выполняет JavaScript, который прокручивает страницу так, чтобы элемент
    # button был видимым в окне браузера. Метод execute_script позволяет выполнить
    # произвольный JavaScript в контексте текущей страницы. 
    # Здесь используется метод scrollIntoView(true), который скроллит
    # страницу так, чтобы элемент был видимым. arguments[0] указывает на элемент,
    # переданный в качестве аргумента в JavaScript, который в данном случае является кнопкой.
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #browser.execute_script("window.scrollBy(0, 100);")

    # кликаем по button
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
