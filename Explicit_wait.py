from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=Chrome()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(5)
driver.maximize_window()
wait = WebDriverWait(driver, 10)



ele=wait.until(EC.element_to_be_selected((By.XPATH,"/html/body/div/div[3]/div/div/div[1]/div[3]/div/p[1]")))
print(type(ele))



