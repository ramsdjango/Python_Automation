from selenium import webdriver
d = webdriver.Chrome()
d = webdriver.Firefox()
#d = webdriver.Ie()

d.get("http://www.gmail.com")
d.maximize_window()
d.find_element_by_xpath("//*[@id='identifierId']").send_keys("ramsanangi")
d.find_element_by_id("identifierNext").click()
d.implicitly_wait(20)
d.find_element_by_name("password").send_keys("12345")
d.find_element_by_xpath("//*[@id='passwordNext']").click()
