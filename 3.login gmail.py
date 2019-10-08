from selenium import webdriver
d2=webdriver.Chrome()
d2.get("https://www.gmail.com")
d2.maximize_window()
d2.find_element_by_name("identifier").send_keys("ramsanangi")
d2.find_element_by_id("identifierNext").click()
