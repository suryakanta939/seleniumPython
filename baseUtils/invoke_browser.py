from selenium import webdriver
import os


class InvokeBrowser():

    def opneBrowser(self,browserName):

        driver=None
        browserName=browserName.lower()
        if browserName=="firefox":
            driver=webdriver.Firefox()
        elif browserName=="chrome":

            workingDir = os.path.dirname(__file__)
            driverDir = "../drivers/"
            chromeEXe = driverDir + "chromedriver.exe"
            driverLocation = os.path.join(workingDir,chromeEXe)
            print(driverLocation)
            driver=webdriver.Chrome(driverLocation)
        driver.get("http://demoqa.com/registration/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver

# workingDir=os.path.dirname(__file__)
# driverDir="../drivers/"
# chromeEXe=driverDir+"chromedriver.exe"
# destnationFile=os.path.join(workingDir,chromeEXe)
# print(destnationFile)



