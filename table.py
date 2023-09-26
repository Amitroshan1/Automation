from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("file:///C:/Users/dell/Desktop/testing/selecode/demo.html")
driver.maximize_window()
sleep(2)
tr_tag=driver.find_elements(By.XPATH,"/html/body/table[17]/tbody/tr")
row=len(tr_tag)
th_tag=driver.find_elements(By.XPATH,"/html/body/table[17]/tbody/tr[1]/th")
col=len(th_tag)
sleep(2)
print(row,col)
print("S.no"+"    "+"firstname"+"     "+"lastname"+"    "+"percentage")
for data in range(2,row+1):
    for item in range(1,col+1):
        value=driver.find_element(By.XPATH,"/html/body/table[17]/tbody/tr["+str(data)+"]/td["+str(item)+"]").text
        print(value,end="         ")
    print()
