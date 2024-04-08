import pytest

from Pageobjects.LoginPage import LoginPage
from utilitites.readproperties import Readconfig
from utilitites.Logger import loggenrator



class TestLogin:
    url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()

    @pytest.mark.sanity
    def test_Login002(self,setup):
        self.Log.info("Test_case 002 is started ")
        self.driver= setup
        self.Log.info("Opening Browser")
        self.LP=LoginPage(self.driver)
        self.Log.info("going to url"+self.url)
        self.driver.get(self.url)
        self.LP.setUserName(self.Email)
        self.Log.info("Entering Email"+self.Email)
        self.LP.setPassword(self.password)
        self.Log.info("Entering Password"+self.password)
        self.LP.clickLogin()
        self.Log.info("Clicking on LoginButton")
        if self.driver.title=="Dashboard / nopCommerce administration":
            self.Log.info("Page_Titile"+self.driver.title)
            self.driver.save_screenshot("C:\\NopCommerce\\Screenshots\\test_Login002_Pass.PNG")
            # time.sleep(2)
            self.Log.info("Clicking on Logout button")
            self.LP.clickLogout()
            assert True
            self.Log.info("Test_case002 is passed")


        else:
            self.Log.info("Page_Titile"+self.driver.title)
            self.driver.save_screenshot("C:\\NopCommerce\\screenshot\\test_login002_Fail.PNG")
            assert False
            self.Log.info("Test_case 002 is Failed")
        self.Log.info("Test_case 002 is completed")

        self.driver.close()
