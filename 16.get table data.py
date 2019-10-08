from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
rows=len(driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[1])"))
cols=len(driver.find_element_by_xpath(""))
print(rows)
print(cols)
