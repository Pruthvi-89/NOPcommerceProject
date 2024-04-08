import time

import pytest

from Pageobjects.AddCustomer import Addcustomer
from Pageobjects.LoginPage import LoginPage

from utilitites.Logger import loggenrator
from utilitites.readproperties import Readconfig

class Test_AddCustomer:
    geturl = Readconfig.geturl()
    getEmail = Readconfig.getEmail()
    getPassword = Readconfig.getpassword()
    Log = loggenrator.Logen()

    @pytest.mark.regression
    def test_addcustomer003(self,setup):
         self.Log.info("Test addcustomer003 is started")
         self.driver = setup
         self.Log.info("Opening Browser")
         self.LP = LoginPage(self.driver)
         self.Log.info("Going To url")
         self.driver.get(self.getEmail)
         self.Log.info("Entering Email--->"+self.getEmail)
         self.LP.setUserName(self.getEmail)
         self.Log.info("Entering Password--->"+self.getPassword)
         self.LP.setPassword(self.getPassword)
         self.Log.info("Click On Login Button")
         self.LP.clickLogin()
         self.AD=Addcustomer(self.driver)
         self.Log.info("Going customer menu Button")
         self.AD.click_on_Customermenu()
         self.Log.info("Click On customer menu Button")
         self.AD.click_On_CustomerButton()
         self.Log.info("click On add customer Button ")
         self.AD.click_OnAdd_Button()
         self.Log.info("Entering Email")
         self.AD.Enter_Emial("pruthvirajDeokate90@gmail.com")
         self.Log.info("Entering Password")
         self.AD.Enter_Password("Deokate@8890")
         self.Log.info("Entering FirstName")
         self.AD.Enter_FirstName("pruthviraj")
         self.Log.info("Entering LastName")
         self.AD.Enter_LastName("Deokate")
         self.Log.info("Entering Gender")
         self.AD.Set_Gender("Male")
         self.Log.info("Entering Date of Birth")
         self.AD.Enter_DOB("11-7-1997")
         self.Log.info("Entering Company Name")
         self.AD.Enter_CompanyName("Sara Spintex India PVT.LTD")
         self.Log.info("Click CheckBox")
         self.AD.Click_Tax_CheckBox()
         self.Log.info("Entering Store Name")
         self.AD.Enter_StoredName("Bajaj Store")
         self.Log.info("Entering Customer Role")
         self.AD.select_CustomerRoleAdmin()
         self.Log.info("Click CheckBox")
         self.AD.click_On_CheckBox()
         self.Log.info("Entering message")
         self.AD.Admin_Comment("Registred Sucessfull")
         self.Log.info("click On Save Button")
         self.AD.Click_On_Save_Button()
         if self.driver.title=="Customers / nopCommerce administration":
              self.driver.save_screenshot("C:\\NopCommerce\\Screenshots\\ADDcustomer_is_Pass.png")
              self.Log.info("Clicking on Logout button")
              self.LP.clickLogout()
              assert True
              self.Log.info("Test addcustomer003 is passed")


         else:
              self.driver.save_screenshot("C:\\NopCommerce\\Screenshots\\ADDcustomer_is_Fail .png")
              assert False
         self.Log.info("Test addcustomer003 is passed")













