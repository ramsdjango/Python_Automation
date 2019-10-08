from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://twitter.com/login")
element=driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/div/label/input")
actionchains=ActionChains(driver)
driver.implicitly_wait(100)
actionchains.double_click(element).perform()
