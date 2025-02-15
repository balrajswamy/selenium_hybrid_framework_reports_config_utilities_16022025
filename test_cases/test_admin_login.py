from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from base_pages.Admin_Login_Page import AdminLoginPage
from utilities.read_properties import Read_Config
from utilities.custom_Logger import Log_Maker


class TestLogin:
    admin_page_url = Read_Config.get_admin_page_url()
    valid_email = Read_Config.get_valid_user_email()
    valid_password = Read_Config.get_valid_user_password()
    logger = Log_Maker.log_gen()


    def invalid_user_id(self):
        from datetime import datetime
        today = datetime.today().strftime("%Y%m%d%H%M%S")
        invalid_user_email = "test_"+str(today)+"@gmail.com"
        return invalid_user_email

    def test_title_verification(self,setup):
        self.logger.info("Title verfication starts")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Account Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
            self.logger.info("Title verfication ends")
        else:
            self.driver.close()
            assert False

    def test_valid_admin_Login(self,setup):
        self.logger.info("test_valid_admin_Login starts")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_login = AdminLoginPage(self.driver)
        self.admin_login.click_my_account_menu()
        time.sleep(1)
        self.admin_login.click_login_menu()
        time.sleep(1)
        self.admin_login.enter_email(self.valid_email)
        time.sleep(1)
        self.admin_login.enter_password(self.valid_password)
        time.sleep(1)
        self.admin_login.click_Login_btn()
        time.sleep(3)
        act_title = self.driver.find_element(By.XPATH,"//div[@id='content']/h2[1]").text

        exp_title = "My Account"

        if act_title == exp_title:
            assert True
            self.driver.close()
            self.logger.info("test_valid_admin_Login ends")
        else:
            self.driver.close()
            assert False


    def test_invalid_admin_Login(self,setup):
        self.logger.info("test_invalid_admin_Login starts")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_login = AdminLoginPage(self.driver)
        self.admin_login.click_my_account_menu()
        time.sleep(1)
        self.admin_login.click_login_menu()
        time.sleep(1)
        invalid_email = self.invalid_user_id()
        self.admin_login.enter_email(invalid_email)
        time.sleep(1)
        self.admin_login.enter_password(self.valid_password)
        time.sleep(1)
        self.admin_login.click_Login_btn()
        time.sleep(3)
        actual_error_message = self.driver.find_element(By.XPATH,'//div[@class="alert alert-danger alert-dismissible"]').text

        exp_error_message = "Warning: No match for E-Mail Address and/or Password."

        if actual_error_message == exp_error_message:
            assert True
            self.driver.close()
            self.logger.info("test_invalid_admin_Login ends")
        else:
            self.driver.close()
            assert False
            self.logger.info("test_invalid_admin_Login ends")



