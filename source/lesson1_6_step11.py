# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try: 
    # �������� ���������� link ������ �� web - ��������
    link = "http://suninjuly.github.io/registration1.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

    # ��� ���, ������� ��������� ������������ ����
    input1 = browser.find_element(By.CSS_SELECTOR, '*.first_block .form-control.first')
    input1.send_keys("Pavel")
    input2 = browser.find_element(By.CSS_SELECTOR, '*.first_block .form-control.second')
    input2.send_keys("Novoselov")
    input3 = browser.find_element(By.CSS_SELECTOR, '*.first_block .form-control.third')
    input3.send_keys("pavel_informatik@vk.com")

    # ���������� ����������� �����
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()