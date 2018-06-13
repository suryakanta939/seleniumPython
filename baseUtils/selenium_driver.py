from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class SeleniumDriver():

    def __init__(self,driver):
        # self.driver=webdriver.Firefox()
        self.driver=driver



    def screenShot(self,resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        currentDir=os.path.dirname(__file__)
        destinationfileName="../screenshots/"+fileName
        destinationfile=os.path.join(currentDir,destinationfileName)
        self.driver.save_screenshot(destinationfile)

    def getByType(self,locatorType):

        locatorType=locatorType.lower()
        try:
            if locatorType=="id":
                return By.ID
            elif locatorType=="name":
                return By.NAME
            elif locatorType=="classname":
                return By.CLASS_NAME
            elif locatorType=="cssselector":
                return By.CSS_SELECTOR
            elif locatorType=="tagname":
                return By.TAG_NAME
            elif locatorType=="xpath":
                return By.XPATH
            elif locatorType=="linktext":
                return By.LINK_TEXT
            elif locatorType=="partiallinktext":
                return By.PARTIAL_LINK_TEXT
        except:
            print("enter the correct name")

    def getElement(self,locatorType,locator):
        element=None
        try:
            locatorType=locatorType.lower()
            byType=self.getByType(locatorType)
            element=self.driver.find_element(byType,locator)
            print("the element found by the locator "+locator)
        except:
            print("the element is not found by the locator "+locator)
            raise NameError("no such " + locator + " present")
        return element

    def getElements(self,locatorType,locator):
        elements=None
        try:
            locatorType=locatorType.lower()
            byType=self.getByType(locatorType)
            elements=self.driver.find_elements(byType,locator)
            print("the element found by the locator "+locator)
        except:
            print("the element is not found by the locator "+locator)
            raise NameError("no such " + locator + " present")
        return elements



    def isElementPresent(self,locatorType,locator):

        elements=self.getElements(locatorType,locator)
        if len(elements)!=0:
            return True
        else:
            return False

    def clickOnElement(self,locatorType,locator):
        self.getElement(locatorType, locator).click()
        print("clciked on the element found by locator " + locator)





    def sendKeys(self,locatorType,locator,data):
        self.getElement(locatorType,locator).send_keys(data)
        print("sent data to the element found by locator " + locator)

    #  ######### Below functins are to perform the action class #############

    def mouseHoverOnElement(self,locatorType,locator):
        act = ActionChains(self.driver)
        act.move_to_element(self.getElement(locatorType,locator)).perform()

    def movetToCordinateOfElement(self,locatorType,locator):

        act=ActionChains(self.driver)
        element=self.getElement(locatorType,locator)
        loc=element.location
        xCord=loc['x']
        ycord=loc['y']
        act.move_by_offset(xCord,ycord).perform()


    def openLinkInNewTab(self,locatorType,locator):

        act=ActionChains(self.driver)
        act.context_click(self.getElement(locatorType,locator)).perform()
        act.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    # ##################################################################

    # ######### BELLOW FUNCTION TO PERFORM THE SELECT CLASS FUNCTION ######

    def selectElementByText(self,locatorType,locator,textToSelect):

        sel=Select(self.getElement(locatorType,locator))
        sel.select_by_visible_text(textToSelect)

    def selectElementByIndex(self,locatorType,locator,index):
        sel=Select(self.getElement(locatorType,locator))
        sel.select_by_index(index)

    def selectElementByValue(self,locatorType,locator,valueToBeSelect):
        sel = Select(self.getElement(locatorType, locator))
        sel.select_by_value(valueToBeSelect)

    def verifyELementFromDropDown(self,locatorType,locator,textToVerify):
        sel=Select(self.getElement(locatorType,locator))
        allOptions=sel.options
        isTextPresent=False
        for option in allOptions:
            if option.text==textToVerify:
                print("text is present in the dropdown box")
                isTextPresent=True
                break
            else:
                continue

        return isTextPresent








    def getAlldropDownOptions(self,locatorType,locator):
        sel = Select(self.getElement(locatorType, locator))
        allOptions = sel.options

        for option in range(0,len(allOptions)):
            print(allOptions[option].text)



    # ##############################################################

    # ########## THIS FUNCTION WILL HELP TO HANDEL THE WINDOW ############

    def handelWindowByWindowNo(self,windowNo):
        handels=self.driver.window_handles
        print("the total no of window is "+str(len(handels)))
        for handel in range(0,len(handels)):
             if handel==windowNo-1:
                 self.driver.switch_to.window(handels[handel])

    def handelWindowByTitle(self,windowTitle):

        pid=self.driver.current_window_handle
        handels=self.driver.window_handles

        for handel in handels:
            if pid!=handel:
                self.driver.switch_to.window(handel)
                Title=self.driver.title
                if Title==windowTitle:
                    self.driver.switch_to.window(handel)


    # #####################################################################


    # ##################### THIS FUNCTIONS BELOW WILL HELP TO HANDEL ALERT ########

    def handelAlertAccept(self):
        Alert=self.driver.switch_to.alert
        Alert.accept()

    def handelAlertCancel(self):
        Alert=self.driver.switch_to.alert
        Alert.dismiss()

    def handelAlertReadText(self):
        Alert=self.driver.switch_to.alert
        alertText=Alert.text
        return alertText

    # ##############################################################

    # ######## THIS FUNCTIONIS TO SCROLL #########################

    def scroll(self,toWhere):
        toWhere=toWhere.lower()
        if toWhere=="up":
            self.driver.execute_script("window.scrollBy(0,-1500);")
        elif toWhere=="down":
            self.driver.execute_script("window.scrollBy(0,1500);")

    def scrollToExactElement(self,locatorType,locator):
        element = self.getElement(locatorType, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-150);")
    # ############################################################

    # ######### THIS FUNCTION WILL HEP TO READ DATA FROM XCEL SHEET#########


