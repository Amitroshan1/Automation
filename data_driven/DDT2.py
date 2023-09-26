from time import sleep
import XLutil
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



driver=Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

path="C:\\Users\\dell\\Desktop\\selenium_test\\data_driven\\Book.xlsx"
row=XLutil.getRowCount(path,'Sheet1')


for item in range(2,row+1):
    # Getting data from EXLsheet
    pric=XLutil.readData(path,"Sheet1",item,1)
    ROI=XLutil.readData(path,"Sheet1",item,2)
    Per1=XLutil.readData(path,"Sheet1",item,3)
    Per2=XLutil.readData(path,"Sheet1",item,4)
    freq=XLutil.readData(path,"Sheet1",item,5)
    print(freq)
    expt_val=XLutil.readData(path,"Sheet1",item,7)

    # Passing data to the application
    driver.find_element(By.XPATH,"//input[@name='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@name='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,"//input[@name='tenure']").send_keys(Per1)

    dropdown=driver.find_element(By.XPATH,"//select[@name='tenurePeriod']")

    alloption=Select(dropdown)
    alloption.select_by_visible_text(Per2)

    ferq_dropdown=driver.find_element(By.XPATH,"//select[@name='frequency']")
    all_option=Select(ferq_dropdown)
    all_option.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    actual_mat_val=driver.find_element(By.XPATH,"//div/span[@class='gL_27']/strong").text
    sleep(2)

    # validation
    if float(expt_val) == float(actual_mat_val):
        print('Test Passed')
        XLutil.writeData(path,"Sheet1",item,8,"Passed")
        XLutil.fillcolor(path,"Sheet1",item,8)
    else:
        print('Test Failed')
        XLutil.writeData(path,"Sheet1",item,8,"Failed")
        XLutil.fillredcolor(path,"Sheet1",item,8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    sleep(2)





