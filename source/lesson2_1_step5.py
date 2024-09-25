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
    link = "https://suninjuly.github.io/math.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

    # ������� ������� � ������������� x_element
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    # �������������� ��������� ������� calc �������� y
    y = calc(x)
   
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
    time.sleep(1)

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
