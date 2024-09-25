# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

# ������� calc
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    # �������� ���������� link ������ �� web - ��������
    link = "http://suninjuly.github.io/get_attribute.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()
    # ��������� � �������� web - ��������
    browser.get(link)

    # ���������� �������� �� id
    element = browser.find_element(By.ID, 'treasure') 

    # ��������� �������� �������� � ������� ������� get_attribute()
    x_element = element.get_attribute('valuex')
    
    # �������������� ��������� ������� calc �������� y
    y = calc(x_element)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    # ������� ������ checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")

    # ������� �� checkbox
    option1.click()

    # ������� ������ radiobutton
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")

    # ������� �� radiobutton
    option2.click()

    # ������� ������� button
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # ������� �� button
    button.click()

    # ������� �������� �������
    time.sleep(5)

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
