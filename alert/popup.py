from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(5)

driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/button[1]").click()
sleep(5)

driver.switch_to.alert.accept()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/button[2]").click()
sleep(2)
driver.switch_to.alert.accept()
sleep(3)
driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/button[2]").click()
sleep(3)
driver.switch_to.alert.dismiss()
sleep(3)
prompt=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/button[3]")
sleep(2)
prompt.click()
sleep(2)
alert=driver.switch_to.alert
alert.send_keys("amit")
sleep(2)
alert.accept()
sleep(5)
