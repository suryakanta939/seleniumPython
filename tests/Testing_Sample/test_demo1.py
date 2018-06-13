import pytest
import unittest

class TestDemo(unittest.TestCase):

    def test_methodA(self):
        print("executing test method A")

    def test_methodB(self):
        print("execuitng test method B")

    def test_methodC(self):
        print("executing test method c")

if __name__=="__main__":
    unittest.main()
