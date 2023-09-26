from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=610644601173&hvpos=&hvnetw=g&hvrand=9407941910834311269&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062068&hvtargid=kwd-10573980&hydadcr=14453_2316415")
driver.maximize_window()
sleep(2)

driver.save_screenshot("C:\\Users\\dell\\Desktop\\selenium_test\\screenshot\\amit.png")

#other commands
driver.get_screenshot_as_file("C:\\Users\\dell\\Desktop\\selenium_test\\screenshot\\Jpg.png")