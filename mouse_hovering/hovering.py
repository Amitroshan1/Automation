from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver=Chrome()
driver.get("https://www.python.org/")
driver.implicitly_wait(10)
driver.maximize_window()
sleep(2)
assert "Python" in driver.title
download=driver.find_element(By.CSS_SELECTOR,"#downloads > a:nth-child(1)")
source=driver.find_element(By.CSS_SELECTOR,"#downloads > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)")

Action=ActionChains(driver)
Action.move_to_element(download).move_to_element(source).click().perform()
sleep(5)