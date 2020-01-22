from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://newtours.demoaut.com//")
#wait some time
driver.implicitly_wait(15)#implicitly wait
assert "Welcome: Mercury Tours" in driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()

#explici wait()

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Firefox()

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")
#driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID,"tab-flight-tab-hp").click()#flights


driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("08/28/2019")

driver.find_element(By.ID,"flight-returning-hp-flight").clear()

driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("08/29/2019")


driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

wait=WebDriverWait(driver,10)

element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))

'''









