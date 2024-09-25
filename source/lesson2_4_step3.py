# -*- coding: utf-8 -*- #”правление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # ѕередаем переменной link ссылку на web - страницу
    link = "http://suninjuly.github.io/wait1.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ¬ Selenium WebDriver есть специальный способ организации такого ожидани€, который позвол€ет
    # задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам.
    # ќжидание называетс€ не€вным (Implicit wait), так как его не надо €вно указывать каждый раз,
    # когда мы выполн€ем поиск элементов, оно автоматически будет примен€тьс€ при вызове каждой
    # последующей команды. “еперь мы можем быть уверены, что при небольших задержках в работе сайта 
    # наши тесты продолжат работать стабильно. 
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    # открываем в браузере web - страницу
    browser.get(link)

    button = browser.find_element(By.ID, "verify")
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождени€ скрипта
    time.sleep(10)
    # закрываем браузер после всех манипул€ций
    browser.quit()
