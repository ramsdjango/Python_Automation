from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("http://www.wikipedia.org/")
driver.maximize_window()
#driver.find_element_by_xpath("//*[@id='searchLanguage']").send_keys("हिन्दी")
#Select(driver.find_element_by_xpath("//*[@id='searchLanguage']")).select_by_visible_text("हिन्दी")
dropdown=driver.find_element_by_xpath("//*[@id='searchLanguage']")


select=Select(dropdown)
select.select_by_value("hi")
dropoption=driver.find_elements_by_tag_name("option")
print( len(dropoption))
for values in dropoption:
    #print(values.text.encode('ascii','ignore').decode('ascii'))
    print(values.get_attribute("Lang"))