import time

from selenium.webdriver.common.by import By

from Pageobjects.AddCustomer import Addcustomer
from Pageobjects.Login import LoginPage
from Pageobjects.SearchEmp import Search_Emp
from utilitites.Logger import loggenrator
from utilitites.readproperties import Readconfig


class Test_empSearch:
    url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()


    def test_empsearch(self,setup):
        self.driver = setup
        self.LP = LoginPage(self.driver)
        self.driver.get(self.url)
        self.LP.enter_email(self.Email)
        self.LP.enter_password(self.password)
        self.LP.click_On_loginButton()
        self.AD = Addcustomer(self.driver)
        self.AD.click_on_Customermenu()
        self.AD.click_On_CustomerButton()
        self.ES = Search_Emp(self.driver)
        self.ES.Enter_FirstName("Pruthviraj")
        self.ES.Enter_Lastname("Deokate")
        self.ES.click_On_search_Button()
        print(self.ES.Search_Result())




