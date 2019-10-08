'''
Alerts dont have any locators
alert is a popup window that comes upon screen(notif just likea window)
there are many user actions that can request in an alert screen
1.simple alert
2.confirmation alert
3.prompt alert
handling alerts using selenium webbrowsing
Events-:
1.Accecpt()-:to accept the alert
2.dismiss()-:to dismiss the alert
3.Text()-:to get the text of the element
4.send keys()-;to write the some text of the alert
'''
from selenium import webdriver
d2=webdriver.Firefox()
d2.maximize_window()
d2.get("https://www.facebook.com")
d2.find_element_by_id("loginbutton").click()
alert=d2.switch_to_alert()
msg=alert.text
print(msg)
alert.accept()