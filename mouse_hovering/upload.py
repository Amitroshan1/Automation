from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key,Controller
from time import sleep

driver = Chrome()
driver.get("https://www.remove.bg/upload")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div/div/div/div[1]/div/div[1]/div[2]/button").click()
sleep(5)

keyboard = Controller()
keyboard.type("C:\\Users\dell\\Downloads\\amit.jpg")
keyboard.press(Key.enter)
keyboard.release(Key.enter)