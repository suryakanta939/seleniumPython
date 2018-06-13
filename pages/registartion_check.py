from baseUtils.selenium_driver import SeleniumDriver

class registration(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _firstName_id="name_3_firstname"
    _lastName_id="name_3_lastname"
    _maritalStatu_elements_xpath_="//input[@type='radio']"
    _hobby_elements_xpath="//input[@type='checkbox']"
    _country_Xpath="//select[@id='dropdown_7']"
    _month_xpath="//select[@id='mm_date_8']"
    _date_xpath="//select[@id='dd_date_8']"
    _year_xpath="//select[@id='yy_date_8']"
    _phone_id="phone_9"
    _username_id="username"
    _email_id="email_1"
    _chooseFile_id="profile_pic_10"
    _about_id="description"
    _password_id="password_2"
    _confirmpassword_id="confirm_password_password_2"
    _submit_name="pie_submit"

    def fillingUpForm(self,firstname,lastName,phoneNo,user,email):
        self.sendKeys("id",self._firstName_id,firstname)
        self.sendKeys("id",self._lastName_id,lastName)
        elements=self.getElements("xpath",self._maritalStatu_elements_xpath_)
        for element in elements:
            element.click()
        checkboxes=self.getElements("xpath",self._hobby_elements_xpath)
        for checkbox in checkboxes:
            checkbox.click()

        self.selectElementByText("xpath",self._country_Xpath,"India")
        self.selectElementByValue("xpath",self._month_xpath,"9")
        self.selectElementByIndex("xpath",self._date_xpath,19)
        self.selectElementByText("xpath",self._year_xpath,"1991")
        self.sendKeys("id",self._phone_id,str(phoneNo))
        self.sendKeys("id",self._username_id,user)
        self.sendKeys("id",self._email_id,email)
        self.sendKeys("id",self._chooseFile_id,"C:\\Users\\surya\\Desktop\\name.xlsx")
        self.sendKeys("id",self._about_id,"hello hi")
        self.sendKeys("id",self._password_id,"reset123")
        self.sendKeys("id",self._confirmpassword_id,"reset")
        self.clickOnElement("name",self._submit_name)