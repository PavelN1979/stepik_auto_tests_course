# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

    # ������� ������� � ������������� x_element
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text

    # �������������� ��������� ������� calc �������� y
    y = fanc(int(x))

    # ������� ���� ��� ����� ����������
    input = browser.find_element(By.CSS_SELECTOR, '#answer')

    # ��������� ��������� � ����
    input.send_keys(y)

    # ������� ������ checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")

    # ������� �� checkbox
    option1.click()

     # ����� execute_script, ����� ������� ��������� � ������� ��������� ���������, ���������� �������.
    browser.execute_script("window.scrollBy(0, 100);")

    # ������� ������ radiobutton
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")

    # ������� �� radiobutton
    option2.click()
    
    # ������� ������� button
    button = browser.find_element(By.TAG_NAME, "button")

    #browser.execute_script("return arguments[0].scrollIntoView(true);", button):
    # ���� ��� ��������� JavaScript, ������� ������������ �������� ���, ����� �������
    # button ��� ������� � ���� ��������. ����� execute_script ��������� ���������
    # ������������ JavaScript � ��������� ������� ��������. 
    # ����� ������������ ����� scrollIntoView(true), ������� ��������
    # �������� ���, ����� ������� ��� �������. arguments[0] ��������� �� �������,
    # ���������� � �������� ��������� � JavaScript, ������� � ������ ������ �������� �������.
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #browser.execute_script("window.scrollBy(0, 100);")

    # ������� �� button
    button.click()

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
