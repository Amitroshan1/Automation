from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("file:///C:/Users/dell/Desktop/testing/selecode/demo.html")
driver.maximize_window()
sleep(3)
# driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')
driver.get("https://www.w3schools.com/python/python_regex.asp")
sleep(2)