from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)

# scrolly the page by pixcels
driver.execute_script("window.scrollBy(0,100)","")
sleep(2)

# to reach the down of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(5)

# to reach the top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
sleep(5)

# Scroll down to element is visible
flag=driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[2]/div/div[2]/h2/a")
driver.execute_script("arguments[0].scrollIntoView();",flag)
sleep(5)