import pytest

from Pageobjects.LoginPage import LoginPage
from utilitites.readproperties import Readconfig
from utilitites.Logger import loggenrator



class TestLogin_Params:
    url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()

    @pytest.mark.sanity
    def test_Login_Parms005(self,setup,getDataforLogin):
        self.Log.info("Test_case 003 is started ")
        self.driver= setup
        self.Log.info("Opening Browser")
        self.LP=LoginPage(self.driver)
        self.Log.info("going to url"+self.url)
        self.driver.get(self.url)
        self.LP.setUserName(getDataforLogin[0])
        self.Log.info("Entering Email"+getDataforLogin[0])
        self.LP.setPassword(getDataforLogin[1])
        self.Log.info("Entering Password"+getDataforLogin[1])
        self.LP.clickLogin()
        self.Log.info("Clicking on LoginButton")

        status_List=[]
        if self.driver.title=="Dashboard / nopCommerce administration":
            if getDataforLogin[2]== "Pass":
                self.Log.info("Page_Titile"+self.driver.title)
                self.driver.save_screenshot("C:\\NopCommerce\\Screenshots\\"+getDataforLogin[0]+"test_Login_Params005_Pass.PNG")
                # time.sleep(2)
                self.Log.info("Clicking on Logout button")
                self.LP.clickLogout()
                self.Log.info("Test_case_Params005 is Passed")
                status_List.append("Pass")


            elif getDataforLogin[2]== "Fail":
                self.Log.info("Page_Titile"+self.driver.title)
                self.driver.save_screenshot("C:\\NopCommerce\\Screenshots\\"+getDataforLogin[0]+"test_Login-Params 005_Failed.PNG")
                # time.sleep(2)
                self.Log.info("Clicking on Logout button")
                self.LP.clickLogout()
                status_List.append("Fail")





        else:
            if getDataforLogin[2]== "Pass":
               self.Log.info("Page_Titile"+self.driver.title)
               self.driver.save_screenshot("C:\\NopCommerce\\screenshot\\"+getDataforLogin[0]+"test_login_Params005_Passed.PNG")
               status_List.append("Fail")

            elif getDataforLogin[2]== "Fail":
               self.Log.info("Page_Titile"+self.driver.title)
               self.driver.save_screenshot("C:\\NopCommerce\\screenshot\\test_login_params005_Fail.PNG")
               status_List.append("Pass")

        if "Fail" not in status_List:
            self.Log.info("Test_Login_params 005 is Passed")
            assert True
        else:
            self.Log.info("Test_Login_params 005 is Failed")
            assert False
        self.Log.info("Test_case_Params 005 is completed")

        self.driver.close()
