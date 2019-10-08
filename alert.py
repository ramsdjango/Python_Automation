from selenium import webdriver
d2=webdriver.Firefox()
d2.maximize_window()
d2.get("https://mail.rediff.com/cgi-bin/login.cgi")
d2.find_element_by_name("proceed").click()
alert=d2.switch_to_alert()
msg=alert.text
print(msg)
#alert.accept()
#alert.dismiss()
#alert.text
#alert.send_keys("please enter to send")
