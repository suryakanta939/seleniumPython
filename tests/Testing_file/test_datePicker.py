import unittest
import pytest
from pages.date_picker_page import DatePicker

@pytest.mark.userfixtures("oneTimeSetUp","setUp")
class testDatePicker(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.dp=DatePicker(self.driver)

    def test_datePicker(self):
        self.dp.selectDate()

