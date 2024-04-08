import time

import pytest

from Pageobjects.LoginPage import LoginPage
from utilitites import xlutilities
from utilitites.readproperties import Readconfig
from utilitites.Logger import loggenrator



class TestLogin:
    url = Readconfig.geturl()
    Log = loggenrator.Logen()
    Path = "C:\\NopCommerce\\Test_Cases\\TestData\\LoginData.xlsx"

    @pytest.mark.sanity
    def test_Login002(self,setup):
        self.Log.info("Test_case 002 is started ")
        self.driver= setup
        self.Log.info("Opening Browser")
        self.LP=LoginPage(self.driver)
        self.Log.info("going to url"+str(self.url))
        self.driver.get(self.url)
        self.Rows = xlutilities.getrowcount(self.Path,"Sheet1")
        print("No of Rows present in Sheet1-->"+str(self.Rows))
        status_List = []
        for r in range(2,self.Rows + 1):
            self.Email = xlutilities.readdata(self.Path,"Sheet1", r, 2 )
            self.password = xlutilities.readdata(self.Path,"Sheet1", r, 3)
            self.Expt_Result = xlutilities.readdata(self.Path,"Sheet1",r,4)

            self.LP.setUserName(self.Email)
            self.Log.info("Entering Email"+str(self.Email))
            self.LP.setPassword(self.password)
            self.Log.info("Entering Password"+str(self.password))
            self.LP.clickLogin()
            self.LP.settingMenu()
            self.LP.clickClearCache()


            self.Log.info("Clicking on LoginButton")
        if self.driver.title == "Dashboard / nopCommerce administration":
            if self.Expt_Result == "Pass":
                self.Log.info("Page_Titile" + str(self.driver.title))
                self.driver.save_screenshot(
                    "C:\\NopCommerce\\Screenshots\\"+self.Email + self.password + "test_Login_Params005_Pass.PNG")
                # time.sleep(2)
                self.Log.info("Clicking on Logout button")
                self.LP.clickLogout()
                self.Log.info("Test_case_Params005 is Passed")
                status_List.append("Pass")
                xlutilities.writedata(self.Path,"Sheet1", r, 2,"Pass" )




            elif self.Expt_Result == "Fail":
                self.Log.info("Page_Titile" + str(self.driver.title))
                self.driver.save_screenshot(
                    "C:\\NopCommerce\\Screenshots\\"+self.Email + self.password + "test_Login-Params 005_Failed.PNG")
                # time.sleep(2)
                self.Log.info("Clicking on Logout button")
                self.LP.clickLogout()
                status_List.append("Fail")
                xlutilities.writedata(self.Path,"Sheet1", r, 2,"Fail" )










            else:
                if  self.Expt_Result == "Pass":
                    self.Log.info("Page_Titile"+(self.driver.title))
                    self.driver.save_screenshot("C:\\NopCommerce\\screenshot\\"+self.Email + self.password +"test_login_Params005_Passed.PNG")
                    status_List.append("Fail")
                    xlutilities.writedata(self.Path, "Sheet1", r, 2, "Fail")



                elif self.Expt_Result == "Fail":
                    self.Log.info("Page_Titile" + str(self.driver.title))
                    self.driver.save_screenshot("C:\\NopCommerce\\screenshot\\"+self.Email + self.password +"test_login_params005_Fail.PNG")
                    status_List.append("Fail")


        print(status_List)
        if "Fail" not in status_List:
            self.Log.info("Test_Login_params 005 is Passed")
            assert True
        else:
            self.Log.info("Test_Login_params 005 is Failed")
            assert False
            self.Log.info("Test_case_Params 005 is completed")

        self.driver.close()
