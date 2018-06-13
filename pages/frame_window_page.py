from baseUtils.selenium_driver import SeleniumDriver

class FrameAndWinodw(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _frame_window_xpath="//a[@href='http://demoqa.com/frames-and-windows/']"
    _newBrowser_tab_xpath="//a[contains(text(),'New Browser Tab')]"
    _registration_xpath = "//a[text()='Registration']"
    _first_name_xpath = "//input[@id='name_3_firstname']"
    _separate_newWINdow_xpath="//a[@id='ui-id-2']"
    _separateWIndowLink_xapth="//a[@href='http://toolsqa.com/registration']"
    _page_not_found_="//h1[text()='Oops! That page can’t be found.']"
    _frame_set_xapth="//a[@id='ui-id-3']"



    def frameWindowCheck(self):
        self.clickOnElement("xpath",self._frame_window_xpath)
        self.clickOnElement("xpath",self._newBrowser_tab_xpath)
        self.handelWindowByWindowNo(2)
        self.clickOnElement("xpath",self._registration_xpath)
        self.sendKeys("xpath",self._first_name_xpath,"hello")
        self.driver.close()
        self.handelWindowByWindowNo(1)
        self.clickOnElement("xpath",self._separate_newWINdow_xpath)
        self.clickOnElement("xpath",self._separateWIndowLink_xapth)
        self.handelWindowByWindowNo(2)
        textmessage=self.getElement("xpath",self._page_not_found_).text
        print(textmessage)
        self.driver.close()
        self.handelWindowByWindowNo(1)
        self.clickOnElement("xpath",self._frame_set_xapth)