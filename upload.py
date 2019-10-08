from selenium import webdriver
driver =webdriver.Chrome()
driver.get("http://www.testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("E:\HG\IMG_0543.JPG")