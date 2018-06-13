import unittest
import pytest
from pages.frame_window_page import FrameAndWinodw
@pytest.mark.usefixture("oneTimeSetUp","setUp")
class testFrameAndWindowHandel(unittest.TestCase):

    @pytest.fixture(autouse=2)
    def classSetUp(self,oneTimeSetUp):
        self.fw=FrameAndWinodw(self.driver)

    def testFrameAndWindow(self):
        self.fw.frameWindowCheck()

