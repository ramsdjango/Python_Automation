''''#scrol down page by pixel
driver.exicute_script("window.scrollBy(0,500)","")
#scroll down by poage till elment found
driver.exicute_script("arguments[0].scrollintoView();",Element)
#scrool to end of the page
driver.exicute_script("window.scrollBy(0,document.body.scrollHeight)")
'''
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
#scrol down page by pixel
#driver.execute_script("window.scrollBy(0,100)","")
#scroll down by poage till elment found
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#scrool to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
