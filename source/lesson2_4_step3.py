# -*- coding: utf-8 -*- #���������� ���������� UTF-8

# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # �������� ���������� link ������ �� web - ��������
    link = "http://suninjuly.github.io/wait1.html"

    # Initialize Chrome WebDriver
    browser = webdriver.Chrome()

    # � Selenium WebDriver ���� ����������� ������ ����������� ������ ��������, ������� ���������
    # ������ �������� ��� ������������� ��������, ����� ��������� ��� �� ���� ������.
    # �������� ���������� ������� (Implicit wait), ��� ��� ��� �� ���� ���� ��������� ������ ���,
    # ����� �� ��������� ����� ���������, ��� ������������� ����� ����������� ��� ������ ������
    # ����������� �������. ������ �� ����� ���� �������, ��� ��� ��������� ��������� � ������ ����� 
    # ���� ����� ��������� �������� ���������. 
    # ������� WebDriver ������ ������ ������� � ������� 5 ������
    browser.implicitly_wait(5)

    # ��������� � �������� web - ��������
    browser.get(link)

    button = browser.find_element(By.ID, "verify")
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()
