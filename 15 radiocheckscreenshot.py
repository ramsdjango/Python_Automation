from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.dyn-web.com/tutorials/forms/examples/pizza.php")
#working with radio buttons
'''status=driver.find_element_by_name("size").is_selected()
print(status)

driver.find_element_by_name("size").click()

status=driver.find_element_by_name("size").is_selected()
print(status)
#working with check boxes
status=driver.find_element_by_name("onions").click()

status=driver.find_element_by_name("onions").is_selected()
print(status)'''

###screenshots
driver.save_screenshot("python.png")
driver.get_screenshot_as_file("python.png")
