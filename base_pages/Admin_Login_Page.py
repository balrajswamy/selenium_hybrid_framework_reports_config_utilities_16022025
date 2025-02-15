from selenium.webdriver.common.by import By
from selenium import webdriver


class AdminLoginPage:
    #locators
    my_acct_link_text = 'My Account'
    my_acct_login_link_text = 'Login'
    email_xpath = '//input[@name="email"]'
    password_xpath = '//input[@name="password"]'
    btn_login_xpath = '//input[@type="submit"]'

    def __init__(self,driver):
        self.driver = driver

    def click_my_account_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.my_acct_link_text).click()
    def click_login_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.my_acct_login_link_text).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_xpath).clear()
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.password_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def click_Login_btn(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

        

