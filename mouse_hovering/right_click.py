from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(5)
driver.maximize_window()
sleep(5)
ele=driver.find_element(By.CSS_SELECTOR,"html body.wy-body-for-nav div.wy-grid-for-nav section.wy-nav-content-wrap div.wy-nav-content div.rst-content div.document p span.context-menu-one.btn.btn-neutral")

action=ActionChains(driver)

action.context_click(ele).perform()
sleep(5)