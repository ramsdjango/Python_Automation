from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source_element=driver.find_element_by_xpath("//*[@id='box6']")
target_element=driver.find_element_by_xpath("//*[@id='box106']")
actionchains=ActionChains(driver)
driver.implicitly_wait(20)
actionchains.drag_and_drop(source_element,target_element).perform()