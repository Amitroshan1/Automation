from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions



option=ChromeOptions()
option.add_experimental_option("prefs",{"download.default_directory":"path"})
driver=Chrome()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(5)
driver.maximize_window()
wait = WebDriverWait(driver, 10)



