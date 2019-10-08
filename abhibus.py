from selenium import webdriver
import time
d2=webdriver.Chrome()
d2.get("https://www.abhibus.com")
d2.maximize_window()
d2.find_element_by_id("source").send_keys("Addanki")

d2.find_element_by_id("destination").send_keys("Visakhapatnam")
d2.find_element_by_class_name("ui-state-default ui-state-active").send_keys("06-09-2019")
time.sleep(5)
d2.find_element_by_class_name("btnab icosearch")