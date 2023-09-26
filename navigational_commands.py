from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.python.org/")
sleep(2)
print(driver.title)
driver.get("https://www.geeksforgeeks.org/webdriver-navigational-commands-forward-and-backward-in-selenium-with-python/")
sleep(2)
print(driver.title)
sleep(2)
driver.back()
print(driver.title)
sleep(2)
driver.forward()
print(driver.title)
driver.refresh()

