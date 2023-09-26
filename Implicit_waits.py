from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver=Chrome()
driver.get("https://www.python.org/")
driver.maximize_window()
driver.implicitly_wait(5)
assert "Python" in driver.title
driver.find_element(By.CSS_SELECTOR,"#downloads > a:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"#downloads > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()