import XLutil
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from  time import sleep

driver= Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.implicitly_wait(5)
driver.maximize_window()

path="C:\\Users\\dell\\Desktop\\testcases.xlsx"

row= XLutil.getRowCount(path,'Sheet1')

for rownum in range(2,row+1):
    username=XLutil.readData(path,'Sheet1',rownum,1)
    password= XLutil.readData(path,'Sheet1',rownum,2)

    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH,"//button[@id='submit']").click()
    sleep(2)

    if driver.title == "Logged In Successfully | Practice Test Automation":
        XLutil.writeData(path,'Sheet1',rownum,3,"test passed")
    else:
        XLutil.writeData(path,'Sheet1',rownum,3,"test failed")
    sleep(5)

    driver.back()
