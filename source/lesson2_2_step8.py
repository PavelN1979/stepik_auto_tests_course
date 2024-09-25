# -*- coding: utf-8 -*- #”правление кодировкой UTF-8

# импортируем пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# стандартный модуль Python дл€ работы с операционной системой Ч os
import os, time

try: 
    # ѕередаем переменной link ссылку на web - страницу
    link = "http://suninjuly.github.io/file_input.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # открываем в браузере web - страницу
    browser.get(link)

     # ¬аш код, который заполн€ет об€зательные пол€
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Pavel")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("Novoselov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("pavel_informatik@vk.com")

    # получаем путь к директории текущего исполн€емого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    
    # добавл€ем к этому пути им€ файла 
    file_path = os.path.join(current_dir, 'file.txt') 
    
     # метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
    browser.execute_script("window.scrollBy(0, 50);")

    # находим кнопку дл€ загрузки файла
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")

    # загружаем файл
    input4.send_keys(file_path)
    
    # находим кнгопку button
    button = browser.find_element(By.TAG_NAME, "button")

    # кликаем по button
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождени€ скрипта
    time.sleep(10)
    # закрываем браузер после всех манипул€ций
    browser.quit()
