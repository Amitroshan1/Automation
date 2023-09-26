from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.maximize_window()

sleep(5)
source= driver.find_element(By.ID,"draggable")
target=driver.find_element(By.ID,"droppable")

action=ActionChains(driver)

action.drag_and_drop(source,target).perform()
sleep(4)