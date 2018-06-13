import unittest
import pytest
from pages.to_check import checking
from ddt import ddt,data,unpack
from commonUtils.redaing_xcel_data import getDataFromXcel
@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class Hello(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        print("running the class setup")
        self.ch=checking(self.driver)

    @data(*getDataFromXcel("D:\\SeleniumPython\\PracticeFWK\\name.xlsx"))
    @unpack
    def test_runCheking(self,firstName,lastName,country,phone,user,email):
        # self.ch.check()
        # self.ch.readOptions()
        print(firstName)
        print(lastName)
        print(country)
        print(phone)
        print(user)
        print(email)
        print("running the after class setup")



