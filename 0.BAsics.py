'''# basic webdriver commands
# capture title of the page
#capture url of the page
#closing and quiting browser
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element_by_name("q").send_keys("sirivennla")
driver.find_element_by_name("q").submit()
time.sleep(5)

#driver.close()#current page
driver.quit()#close all tabs

#Navigation commands

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.get("https://www.facebook.com")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)
'''
'''#conditional commands
1.is_displayed#any kind of web elements
2.is_enabled#any kind of web elements
3.is_selected#checkbox and radio buttons
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.get("https://www.bingo.com")

driver.close()