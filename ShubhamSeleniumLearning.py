from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.find_element_by_Xpath("//input[@name='email']")
sleep(10)
username_box.send_keys(sjbhau@gmail.com)

