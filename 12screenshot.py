from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.save_screenshot("ram.png")