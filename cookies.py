from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver=Chrome()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=610644601173&hvpos=&hvnetw=g&hvrand=9407941910834311269&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062068&hvtargid=kwd-10573980&hydadcr=14453_2316415")
driver.maximize_window()
sleep(2)

#capture all cookies
cook=driver.get_cookies()
print(len(cook),cook)

# Adding new cookie to browser
cookie={"name":"love","value":'123456'}
driver.add_cookie(cookie)

# deleting the cookie
driver.delete_cookie("love")

#deleting all cookies
driver.delete_all_cookies()
sleep(2)