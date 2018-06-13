from baseUtils.selenium_driver import SeleniumDriver
import time

class checking(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)




    def check(self):
        self.openLinkInNewTab("id","opentab")
        self.scrollToExactElement("id", "mousehover")
        self.mouseHoverOnElement("id", "mousehover")
        time.sleep(1)
        self.clickOnElement("xpath","//a[text()='Reload']")
        time.sleep(1)
        self.scroll("down")

    def readOptions(self):
        self.getAlldropDownOptions("id","multiple-select-example")
        result=self.verifyELementFromDropDown("id","multiple-select-example","Orange")
        print(result)
        assert result==True
