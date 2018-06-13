import pytest
import unittest

class TestDemo2(unittest.TestCase):

    def test_methodA1(self):
        print("executing test method A1")

    def test_methodB1(self):
        print("execuitng test method B1")

    def test_methodC1(self):
        print("executing test method c1")

if __name__=="__main__":
    unittest.main()
