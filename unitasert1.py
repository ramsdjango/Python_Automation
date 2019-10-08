import unittest
from selenium import webdriver



class Test(unittest.TestCase):
    def tes_tname(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com")
        titleOfWebpage=driver.title

        #self.assertEqual("google",titleOfWebpage,"webpage title are not same")
        #self.asserNotEqual("google",titleofwebpage)

        #self.assertTrue(titleOfWebpage=="google")
        #self.assertFalse(titleOfWebpage=="google")

        driver=None
        #self.assertIsNone(driver)
        #self.assertIsNotNone(driver)

class Test(unittest.TestCase):
    def testname(self):
        list=("python","selenium","java")
        #self.assertIn("python",list)
        #self.assertIn("Ruby",list)
        #self.assertNotIn("python",list)
        #self.assertNotIn("Ruby",list)

        #self.assertgreter(100,10)
        #self.assertgreterEqualto(100,100)

        #self.assertless(100,100)
        #self.assertlessEqual(10,10)

if __name__ == '__main__':
    unittest.main()
