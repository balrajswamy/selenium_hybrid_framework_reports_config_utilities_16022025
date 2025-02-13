from selenium.webdriver.common.by import By
from selenium import webdriver


class AdminLoginPage:
    #locators
    email_xpath = '//input[@type="email"]'
    password_xpath = '//input[@type="password"]'
    btn_login_xpath = '//button[@type="submit"]'

    def __init__(self,driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_xpath).clear()
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.password_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

        

