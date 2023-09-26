from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()
sleep(2)


driver.switch_to.frame("frm1")
dropdown=driver.find_element(By.XPATH,"//*[@id='selectnav1']")
s=Select(dropdown)
s.select_by_visible_text("- SQL")
sleep(5)