from baseUtils.selenium_driver import SeleniumDriver
import time

class DatePicker(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _datePicker_xapth="//a[text()='Datepicker']"
    _animation_xpath="//a[text()='Animations']"
    _date_xpath="//input[@id='datepicker2']"
    _animationSlect_xapth="//select[@id='anim']"
    selectDate="//div[div[div[span[text()='{0}']]]]//a[@class='ui-state-default' and text()='{1}']"
    _selectDate_xpath=selectDate.format("September","25")


    def selectDate(self):
        self.clickOnElement("xpath",self._datePicker_xapth)
        self.clickOnElement("xpath",self._animation_xpath)
        self.clickOnElement("xpath",self._date_xpath)
        self.handelCalender()
        self.selectElementByText("xpath",self._animationSlect_xapth,"Fade in")


    def handelCalender(self):

        while True:
            try:
                self.clickOnElement("xpath",self._selectDate_xpath)
                break
            except:
                self.clickOnElement("xpath","//span[@class='ui-icon ui-icon-circle-triangle-e']")
                time.sleep(1)



