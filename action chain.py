from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
d2=webdriver.Firefox()
d2.maximize_window()
d2.get("https://www.google.co.in")
ele=d2.find_element_by_link_text("About")

ActionChains(d2).move_to_element(ele).context_click(ele).perform()
ActionChains(d2).send_keys(Keys.ARROW_DOWN).perform()
ActionChains(d2).send_keys(Keys.ENTER).perform()
