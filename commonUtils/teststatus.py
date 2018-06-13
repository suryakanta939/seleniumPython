from baseUtils.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):

    def __init__(self,driver):
        super(TestStatus,self).__init__(driver)
        self.resultList=[]

    def setResult(self,result,resultMessage):
        try:
           if result is not None:
               if result:
                   self.resultList.append("PASS")
                   print("*********VERIFICATION SUCCESSFULL***********"+resultMessage)

               else:
                   self.resultList.append("FAIL")
                   print("*********VERIFICATION FAILED***********"+resultMessage)
                   self.screenShot(resultMessage)
           else:
               self.resultList.append("FAIL")
               print("*********VERIFICATION FAILED***********"+resultMessage)
               self.screenShot(resultMessage)

        except:
            self.resultList.append("FAIL")
            print("*********VERIFICATION FAILED***********"+resultMessage)
            self.screenShot(resultMessage)

    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)


    def markFinal(self,testName,result,resultMessage):

        self.setResult(result,resultMessage)


        if "FAIL" in self.setResult():

            print(testName + "*********VERIFICATION FAILED***********")
            self.resultList.clear()
            assert True==False
        else:
            print(testName + "*********VERIFICATION SUCCESSFULL***********")
            self.resultList.clear()
            assert True==True