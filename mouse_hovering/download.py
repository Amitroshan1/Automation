from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions
chroemotion = ChromeOptions()
chroemotion.add_experimental_option("prfes",{"download.default_directory":"path"})

driver=Chrome(chroemotion)
driver.get("https://getsamplefiles.com/sample-audio-files/mp3")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/main/main/div/div[2]/div/ul/li[1]/div/div[2]/a").click()
sleep(3)
driver.find_element(By.XPATH,"/html/body/main/main/div/div[2]/div/ul/li[2]/div/div[2]/a").click()
sleep(5)
