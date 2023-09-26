from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=Chrome()
driver.get("https://www.redbus.com/")
driver.maximize_window()
dest=driver.find_element(By.ID,"src")
print(dest.is_enabled())
print(dest.is_displayed())
dest.click()
print(dest.is_selected())
sleep(3)




sleep(2)
