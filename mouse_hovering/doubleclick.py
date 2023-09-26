from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
sleep(3)
ele=driver.find_element(By.CSS_SELECTOR,"#HTML10 > div:nth-child(2) > button:nth-child(6)")
action=ActionChains(driver)
action.double_click(ele).perform()
sleep(3)
