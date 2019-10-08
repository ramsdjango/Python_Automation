import unittest
def setUpModule():#it will be exicuted before exicuting any class or any method before present in he test class
    print("setup module")
def tearDownodule():  #it will be exicuted After exicuting any class or any method before present in he test class
    print("tear town module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):#it exicutes before all tesst method
        print("this is login test")
    @classmethod
    def tearDown(self):#it exicutes After all tesst method
        print("this is  logout test")
    @classmethod
    def setUpclass(self):#it exicutes once class started
        print("Open Apllications")
    @classmethod
    def tearDownclass(self):#it exicutes once class ended
        print("close Application")
    def test_search(self):
        print("this is search")
    def test_advancedsearch(self):
        print("this is advanced search")
    def test_prepaid(self):
        print("this is prepaid recharge")
    def test_postpaid(self):
        print("this is postpaid")



