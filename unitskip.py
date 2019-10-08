import unittest

class Apptest(unittest.TestCase):
    @unittest.SkipTest #decorator
    def test_search(self):
        print("this is search test")
    @unittest.skip("iam skiipi this test")
    def test_advanced(self):
        print("this is advanced")
    @unittest.skipIf(1==1,"one eqials to one")
    def test_preapaid(self):
        print("this is prepaid")
    def test_poatpaid(self):
        print("this poastpaid")
if __name__ == '__main__':
    unittest.main()
