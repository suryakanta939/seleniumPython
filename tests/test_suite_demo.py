import unittest
from tests.Testing_file.test_datePicker import testDatePicker
from tests.Testing_file.test_frame_window import testFrameAndWindowHandel
from tests.Testing_file.test_demo_qa import testDemoQa
from tests.Testing_Sample.test_demo2 import TestDemo2
from tests.Testing_Sample.test_demo1 import TestDemo


testcase1=unittest.TestLoader().loadTestsFromTestCase(testDatePicker)
testcase2=unittest.TestLoader().loadTestsFromTestCase(testFrameAndWindowHandel)
testcase3=unittest.TestLoader().loadTestsFromTestCase(testDemoQa)

testcase4=unittest.TestLoader().loadTestsFromTestCase(TestDemo2)
testcase5=unittest.TestLoader().loadTestsFromTestCase(TestDemo)

smokeTest=unittest.TestSuite([testcase1,testcase2])
regtest=unittest.TestSuite([testcase3])
functest=unittest.TestSuite([testcase4,testcase5])

unittest.TextTestRunner().run(smokeTest)
unittest.TextTestRunner().run(regtest)
unittest.TextTestRunner().run(functest)