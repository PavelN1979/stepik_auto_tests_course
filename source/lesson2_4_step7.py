# -*- coding: utf-8 -*- #Управление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try: 
    # Передаем переменной link ссылку на web - страницу
    link = "http://suninjuly.github.io/wait2.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()
       
    # открываем в браузере web - страницу
    browser.get(link)

    # Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться,
    # когда кнопка станет кликабельной. Для реализации подобных ожиданий в Selenium WebDriver 
    # существует понятие явных ожиданий (Explicit Waits), которые позволяют задать специальное
    # ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью 
    # инструментов WebDriverWait и expected_conditions.
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()

    # Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то
    # можно задать негативное правило с помощью метода until_not:
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    # button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))


    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
