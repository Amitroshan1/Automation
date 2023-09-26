from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("file:///C:/Users/dell/Desktop/testing/selecode/demo.html")
driver.maximize_window()
sleep(3)

driver.find_element(By.XPATH,"/html/body/table[10]/tbody/tr[2]/td/a").click()
sleep(2)

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title=='Demo Web Shop':
        driver.close()
sleep(5)

