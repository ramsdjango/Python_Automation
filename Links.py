from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://newtours.demoaut.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print("no of links present in web page:",len(links))
for i in links:
    print(i.text)
#cliking on the links
driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
