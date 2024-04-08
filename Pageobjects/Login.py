import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException as EC



class LoginPage:

    Text_Enter_Email_XPATH=(By.XPATH,"//input[@id='Email']")
    Text_Enter_password_XPATH=(By.XPATH,"//input[@id='Password']")
    Text_click_On_Login_Button_XPATH=(By.XPATH,"//button[@type='submit']")
    Text_Click_On_Logout_Button_XPATH=(By.CSS_SELECTOR,".main-header.navbar.navbar-expand-md.navbar-dark.bg-dark")



    def __init__(self,driver):
        self. driver  = driver
        self.wait =WebDriverWait(self.driver,10,poll_frequency=0.5)


    def enter_email(self,Email):
             time.sleep(10)
             self.driver.find_element(*LoginPage.Text_Enter_Email_XPATH).clear()
             self.driver.find_element(*LoginPage.Text_Enter_Email_XPATH).send_keys(Email)




    def enter_password(self,password):
        self.driver.find_element(*LoginPage.Text_Enter_password_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Enter_password_XPATH).send_keys(password)


    def click_On_loginButton(self):
        self.driver.find_element(*LoginPage.Text_click_On_Login_Button_XPATH).click()


    def click_On_Logout_Butoon(self):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='fas fa-cogs']")))
        self.driver.find_element(*LoginPage.Text_Click_On_Logout_Button_XPATH).click()

