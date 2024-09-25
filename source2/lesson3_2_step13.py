# coding: latin-1


import unittest
# ����������� ����� Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_search_in_python_org(self): 
        self.browser = webdriver.Chrome()
        browser = self.browser

        browser.get("http://suninjuly.github.io/registration1.html")

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
        assert "Congratulations! You have successfully registered!" == welcome_text

        self.browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "first and second are not equal")
        
    def test_search_in_python_org2(self): 
        self.browser = webdriver.Chrome()
        browser = self.browser

        browser.get("http://suninjuly.github.io/registration2.html")

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
        
        self.browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "first and second are not equal")
        
if __name__ == "__main__":
    unittest.main()

