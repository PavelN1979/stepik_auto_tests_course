# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def fanc(x):
    return math.log(abs(12*math.sin(x)))


try: 
    # �������� ���������� link ������ �� web - ��������
    link = "http://suninjuly.github.io/explicit_wait2.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

    # ����� ���� ��� ��������, ��� ����� �� ������ ����� ������ �� ��������, �� � ���������,
    # ����� ������ ������ ������������. ��� ���������� �������� �������� � Selenium WebDriver 
    # ���������� ������� ����� �������� (Explicit Waits), ������� ��������� ������ �����������
    # �������� ��� ����������� ��������. ������� ����� �������� ����������� � ������� 
    # ������������ WebDriverWait
    # ������� Selenium ����� ��������� ��������� $100 � ����� ����� ���������� ��������
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # ������� ������� button
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn")

    # ������� �� button
    button.click()

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
    button = browser.find_element(By.ID, "solve")

    # ������� �� button
    button.click()


finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
