# -*- coding: utf-8 -*- #���������� ���������� UTF-8
# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # �������� ���������� link ������ �� web - ��������
    link = "https://suninjuly.github.io/selects1.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

    # ���������� �������� �� id
    element = browser.find_element(By.ID, 'num1') 
    element2 = browser.find_element(By.ID, 'num2') 

    # ��������� �������� c �������(.text) � ���������� ������� � ���� int
    y = int(element.text) + int(element2.text)

    # ������� ���� ��� ����� ����������
    input1 = browser.find_element(By.CSS_SELECTOR, '#dropdown')
    # ��������� ��������� � ����
    input1.send_keys(y)

    # ���������� ����������� �����
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()


    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()