from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions


optn=ChromeOptions()
optn.add_argument("--headless")
driver=Chrome(options=optn)
driver.get("file:///C:/Users/dell/Desktop/testing/selecode/demo.html")
driver.maximize_window()
sleep(3)

driver.find_element(By.XPATH,"/html/body/table[10]/tbody/tr[2]/td/a").click()
sleep(2)

handles=driver.window_handles
driver.switch_to.window(handles[0])
sleep(2)
driver.switch_to.window(handles[1])
sleep(1)

driver.switch_to.new_window('window')
driver.get("https://testautomationpractice.blogspot.com/")
sleep(5)

