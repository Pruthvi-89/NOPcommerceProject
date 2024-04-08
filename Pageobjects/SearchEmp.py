from selenium.webdriver.common.by import By


class Search_Emp:

    Text_Enter_FirstNName_Xpath=(By.XPATH,"//input[@id='SearchFirstName']")
    Text_Enter_LastName_Xpath=(By.XPATH,"//input[@id='SearchLastName']")
    Text_Click_On_Search_Button_Xpath=(By.XPATH,"//button[@id='search-customers']")
    Search_Result_xpath=(By.CSS_SELECTOR,"div[class='dataTables_scrollHead'] th:nth-child(2)")


    def __init__(self,driver):
        self.driver = driver

    def Enter_FirstName(self,FirstName):
        self.driver.find_element(*Search_Emp.Text_Enter_FirstNName_Xpath).send_keys(FirstName)

    def Enter_Lastname(self,LastName):
        self.driver.find_element(*Search_Emp.Text_Enter_LastName_Xpath).send_keys(LastName)




    def click_On_search_Button(self):
        self.driver.find_element(*Search_Emp.Text_Click_On_Search_Button_Xpath).click()



    def Search_Result(self):
        search = self.driver.find_elements(*Search_Emp.Search_Result_xpath)
        search_len = len(search)
        if search == 0:
            return True

        elif search_len == 0:
            self.driver.find_element(*Search_Emp.Search_Result_xpath).text
            retrun = False













