import time

import selenium
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_user_id = "Email"
    textbox_password_id_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "Logout"
    settingmenu_Xpath = "//i[@class='fas fa-cogs']"
    clearcache_xpath = "//span[normalize-space()='Clear cache']"



    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_user_id).clear()
        self.driver.find_element(By.ID, self.textbox_user_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def settingMenu(self):
        self.driver.find_element(By.XPATH, self.settingmenu_Xpath).click()

    def clickClearCache(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.clearcache_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
