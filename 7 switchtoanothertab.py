from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
driver.get("http://www.google.com")
driver.maximize_window()

body=driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get("http://www.bing.com")
time.sleep(3)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL +Keys.PAGE_UP)
time.sleep(2)

driver.find_element_by_tag_name(body).send_keys(Keys.CONTROL + 'W')