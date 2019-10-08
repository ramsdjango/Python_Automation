'''from selenium import webdriver
d2=webdriver.Chrome()
d2.maximize_window()
d2.get("https://mail.rediff.com/cgi-bin/login.cgi")
d2.find_element_by_id("login1").send_keys("RAM")
s=d2.find_element_by_id("login1").get_attribute("value")
print(s)

from selenium import webdriver
d2=webdriver.Firefox()
d2.get("https://www.google.com")
d2.find_element_by_name("q").send_keys("man")
d2.find_element_by_name("q").submit()

 #single checkbox
1.input
2.type
3.checkbox


from selenium import webdriver
d2=webdriver.Chrome()
d2.maximize_window()
d2.get("https://mail.rediff.com/cgi-bin/login.cgi")
#d2.find_element_by_xpath("//*[@id='remember']").click()
d2.find_element_by_xpath("//input[@type='checkbox']").click()

#choice for position
from selenium import webdriver
d2=webdriver.Chrome()
d2.maximize_window()
d2.get("http://ironspider.ca/forms/checkradio.htm")
#d2.find_element_by_xpath("//*[@id='remember']").click()
#d2.find_element_by_xpath("(//input[@type='checkbox'])[position()=2]").click()
d2.find_element_by_xpath("(//input[@type='checkbox'])[last()]").click()
'''
#multiple checkboxes

from selenium import webdriver
d2=webdriver.Chrome()
d2.maximize_window()
d2.get("http://ironspider.ca/forms/checkradio.htm")
col_list=d2.find_elements_by_name("color")
for item in col_list:
    val=item.get_attribute("value")
    print(val)

#d2.find_element_by_xpath("//*[@id='remember']").click()
#d2.find_element_by_xpath("(//input[@type='checkbox'])[position()=2]").click()
#d2.find_element_by_xpath("(//input[@type='checkbox'])[last()]").click()
