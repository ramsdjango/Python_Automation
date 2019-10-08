from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com")
print("Title is :",driver.title)
driver.get("https://www.bing.com")
print("Title is :",driver.title)

print("After navigation back:",driver.title)
driver.back()
print("After moving back:",driver.title)
driver.forward()
print("After refreshing :",driver.title)
driver.refresh()