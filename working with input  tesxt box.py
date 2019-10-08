from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi?mobilelogin=1")
#how to find how many input boxes
inputboxes=driver.find_elements(By.XPATH,"/html/body/table[2]")
print(len(inputboxes))