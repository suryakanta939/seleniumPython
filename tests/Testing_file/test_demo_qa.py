import unittest
import pytest
from ddt import ddt,data,unpack
from pages.registartion_check import  registration
from commonUtils.redaing_xcel_data import getDataFromXcel
from commonUtils.reading_csv_data import readData


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class testDemoQa(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.demo=registration(self.driver)


    @data(*readData("D:\\SeleniumPython\\PracticeFWK\\testdat.csv"))
    @unpack
    def test_registration_csv(self,fn,ln,pn,userName,emailId):
        self.demo.fillingUpForm(fn,ln,pn,userName, emailId)


    @data(*getDataFromXcel("D:\\SeleniumPython\\PracticeFWK\\name.xlsx"))
    @unpack
    def test_registration_excel(self, fn, ln, pn, userName, emailId):
        self.demo.fillingUpForm(fn, ln, pn, userName, emailId)


    def tearDown(self):
        self.driver.refresh()