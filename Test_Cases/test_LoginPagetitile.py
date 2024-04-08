from utilitites.Logger import loggenrator
from utilitites.readproperties import Readconfig


class Test_Login:
    url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()


    def test_pagtitile001(self,setup):
        self.Log.info("Test_case001 is started ")
        self.driver = setup
        self.Log.info("Oepning Browser")
        self.driver.get(self.url)
        self.Log.info("Going to url"+self.url)
        if self.driver.title== "Your store. Login":
            self.Log.info("Page Titile"+self.driver.title)
            self.driver.save_screenshot("C:\\NopCommerce\\Screenshotstest_pagtitile002_Passed.PNG")
            assert True
            self.Log.info("Test_case 001 is passed")

        else:
            self.Log.info("Page Titile"+self.driver.title)
            self.driver.save_screenshot("C:\\NopCommerce\\Screenshotstest_pagtitile002_Failed.PNG")
            assert False
            self.Log.info("Test_case 001 is Failed")
        self.Log.info("Test_case 001 is completed")


