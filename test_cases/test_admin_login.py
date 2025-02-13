from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from base_pages.Admin_Login_Page import AdminLoginPage


class TestLogin:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    valid_email = "admin@yourstore.com"
    valid_password = "admin"
    invalid_email = "admin2@yourstore.com"

    def test_title_verification(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_Login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login = AdminLoginPage(self.driver)
        self.admin_login.enter_email(self.valid_email)
        self.admin_login.enter_password(self.valid_password)
        self.admin_login.click_Login()
        time.sleep(18)

        act_title = "Dashboard"
        exp_title = self.driver.title

        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_Login.png")
            self.driver.close()

    def test_invalid_admin_Login(self,setup):
        self.driver = setup

        self.driver.get(self.admin_page_url)
        self.admin_login = AdminLoginPage(self.driver)
        self.admin_login.enter_email(self.invalid_email)
        self.admin_login.enter_password(self.valid_password)
        self.admin_login.click_Login()
        time.sleep(3)
        error_message = "No customer account found"
        act_error_message = self.driver.find_element(By.XPATH,"//ul/li").text
        if error_message == act_error_message:
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()









