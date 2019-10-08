from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Firefox()
driver.get('http://wikipedia.org')
driver.maximize_window()
element=driver.find_element_by_link_text('Wikinews')
hover=ActionChains(driver).move_to_element(element)
hover.perform()