from selenium.webdriver.common.by import By


class Addcustomer:

    Text_Click_On_Customer_Menu_Xpath=(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    Text_Click_On_Customer_Button_Xpath=(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Click_On_AddNew_Button_Xpath=(By.XPATH,"//a[@class='btn btn-primary']")
    Enter_Email_Xpath=(By.XPATH,"//input[@id='Email']")
    Enter_Password_Xpath=(By.XPATH,"//input[@id='Password']")
    Enter_FirstName_Xpath=(By.XPATH,"//input[@id='FirstName']")
    Enter_LastName_Xpath=(By.XPATH,"//input[@id='LastName']")
    Select_Gender_Male_Xpath=(By.XPATH,"//label[@for='Gender_Male']")
    Select_Gender_Female_Xpath=(By.XPATH,"//input[@id='Gender_Female']")
    Enter_Date_of_Birth_Xpath=(By.XPATH,"//input[@id='DateOfBirth']")
    Enter_Company_Name_Xpath=(By.XPATH,"//input[@id='Company']")
    Tax_Exempt_CheckBox_Xpath=(By.XPATH,"//input[@id='IsTaxExempt']")
    Enter_Store_Name_Xpath=(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    Select_Customer_Role_Registred_=(By.XPATH,"//li[normalize-space()='Registered']")
    click_On_check_Box_Xpath=(By.XPATH,"//input[@id='Active']")
    Admin_Comment_Xpath=(By.XPATH,"//textarea[@id='AdminComment']")
    Click_On_Save_Button_Xpath=(By.XPATH,"//button[@name='save']")
    customer_search_Page_Xpath=(By.XPATH,"//h1[@class='float-left']")


    def __init__(self,driver):
        self. driver = driver


    def click_on_Customermenu(self):
        self.driver.find_element(*Addcustomer.Text_Click_On_Customer_Menu_Xpath).click()

    def click_On_CustomerButton(self):
        self.driver.find_element(*Addcustomer.Text_Click_On_Customer_Button_Xpath).click()

    def click_OnAdd_Button(self):
        self.driver.find_element(*Addcustomer.Click_On_AddNew_Button_Xpath).click()

    def Enter_Emial(self,Email):
        self.driver.find_element(*Addcustomer.Enter_Email_Xpath).send_keys(Email)

    def Enter_Password(self,Password):
        self.driver.find_element(*Addcustomer.Enter_Password_Xpath).send_keys(Password)

    def Enter_FirstName(self, Firstname):
        self.driver.find_element(*Addcustomer.Enter_FirstName_Xpath).send_keys(Firstname)


    def Enter_LastName(self,LastName):
        self.driver.find_element(*Addcustomer.Enter_LastName_Xpath).send_keys(LastName)

    def Set_Gender(self,gender):
        if gender == "Male":
            self.driver.find_element(*Addcustomer.Select_Gender_Male_Xpath).click()

        elif gender == "Female":
            self.driver.find_element(*Addcustomer.Select_Gender_Female_Xpath).click()

        else:
            self.driver.find_element(*Addcustomer.Select_Gender_Male_Xpath).click()



    def Enter_DOB(self,DOB):
        self.driver.find_element(*Addcustomer.Enter_Date_of_Birth_Xpath).send_keys(DOB)


    def Enter_CompanyName(self,Co_Name):
        self.driver.find_element(*Addcustomer.Enter_Company_Name_Xpath).send_keys(Co_Name)


    def Click_Tax_CheckBox(self):
        self.driver.find_element(*Addcustomer.Tax_Exempt_CheckBox_Xpath).click()

    def Enter_StoredName(self,StoreName):
        self.driver.find_element(*Addcustomer.Enter_Store_Name_Xpath).send_keys(StoreName)


    def select_CustomerRoleAdmin(self):
        self.driver.find_element(*Addcustomer.Select_Customer_Role_Registred_).click()



    def click_On_CheckBox(self):
        self.driver.find_element(*Addcustomer.click_On_check_Box_Xpath).click()


    def Admin_Comment(self,comment):
        self.driver.find_element(*Addcustomer.Admin_Comment_Xpath).send_keys(comment)


    def Click_On_Save_Button(self):
        self.driver.find_element(*Addcustomer.Click_On_Save_Button_Xpath).click()




