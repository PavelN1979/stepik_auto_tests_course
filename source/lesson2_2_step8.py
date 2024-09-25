# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# ����������� ������ Python ��� ������ � ������������ �������� � os
import os, time

try: 
    # �������� ���������� link ������ �� web - ��������
    link = "http://suninjuly.github.io/file_input.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # ��������� � �������� web - ��������
    browser.get(link)

     # ��� ���, ������� ��������� ������������ ����
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Pavel")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("Novoselov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("pavel_informatik@vk.com")

    # �������� ���� � ���������� �������� ������������ ����� 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    
    # ��������� � ����� ���� ��� ����� 
    file_path = os.path.join(current_dir, 'file.txt') 
    
     # ����� execute_script, ����� ������� ��������� � ������� ��������� ���������, ���������� �������.
    browser.execute_script("window.scrollBy(0, 50);")

    # ������� ������ ��� �������� �����
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")

    # ��������� ����
    input4.send_keys(file_path)
    
    # ������� ������� button
    button = browser.find_element(By.TAG_NAME, "button")

    # ������� �� button
    button.click()

    # ���� �������� ��������
    time.sleep(1)

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
