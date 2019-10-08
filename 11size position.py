from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://en.wikipedia.org")

time.sleep()
#driver.set_window_size(420,480)
driver.set_window_position(150,200)