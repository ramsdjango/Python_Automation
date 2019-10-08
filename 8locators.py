'''2.Element identifiers

ID
name
linkText
CSS selector
partiallinkText and
XPath'''
from selenium import webdriver
d2=webdriver.Chrome()
d2.get("https://www.gmail.com")
d2.maximize_window()
d2.find_element_by_name("identifier").send_keys("ramsanangi")
d2.find_element_by_id()
d2.find_element_by_name()
d2.find_elements_by_tag_name()
d2.find_element_by_xpath()
d2.find_element_by_link_text()
d2.find_element_by_class_name()
d2.find_elements_by_css_selector()
d2.find_elements_by_partial_link_text()