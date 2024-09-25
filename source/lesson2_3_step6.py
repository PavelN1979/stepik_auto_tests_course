# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))


try: 
    # �������� ���������� link ������ �� web - ��������
    link = "http://suninjuly.github.io/redirect_accept.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

    # ������� ������� button
    button = browser.find_element(By.TAG_NAME, "button")

    # ������� �� button
    button.click()

    # ����� ������ ��� ����� �������, ����� ������������ ����� window_handles, ������� ����������
    #  ������ ��� ���� �������.����, ��� � �������� ������ ������� ��� �������, �������� ������ �������:
    new_window = browser.window_handles[1]

    # ��� ������������ �� ����� ������� ���� ���� �������, �� ����� ������� �� ����� �������.
    # ��� �������� � ������� ������� switch_to.window
    browser.switch_to.window(new_window)

    # ����� �� ����� ��������� ��� ������� �������, ����� ����� ����������� ����� � ��� ���������:
    # first_window = browser.window_handles[0]

    # ������� ������� � ������������� x_element
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text

    # �������������� ��������� ������� calc �������� y
    y = fanc(int(x))
    
    # ������� ���� ��� ����� ����������
    input = browser.find_element(By.CSS_SELECTOR, '#answer')

    # ��������� ��������� � ����
    input.send_keys(y)

    # ������� ������� button
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn")

    # ������� �� button
    button.click()

    # ���� �������� ��������
    time.sleep(1)

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
