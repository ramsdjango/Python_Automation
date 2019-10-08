'''from selenium import webdriver

import time
driver=webdriver.Chrome()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to_default_content()


driver.switch_to_frame("packageFrame")#second
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)
driver.switch_to_default_content()

driver.switch_to_frame("classFrame")#second
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
driver.switch_to_default_content()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a").click()
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
driver.quit()