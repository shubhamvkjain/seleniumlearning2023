import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

time.sleep(5)

driver.find_element("id", "email").send_keys('7276152099')
driver.find_element("id", "pass").send_keys('masterkanha')
driver.find_element("name", "login").click()
time.sleep(10)

