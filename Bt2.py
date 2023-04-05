from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome(executable_path="./chromedriver.exe")
     
driver.get("https://www.facebook.com/")
# ===================================================id 
# cach 1 
# txtemail = driver.find_element(By.ID,"email")
# cach2 
# txtemail = driver.find_element_by_id("email")
# txtpassword = driver.find_element_by_id("pass")
# ====================================================name
# cach 1 
# txtemail = driver.find_element(By.NAME,"email")
# cach2 
# txtemail = driver.find_element_by_name("email")
# txtpassword = driver.find_element_by_name("pass")
# ====================================================xpath
# cach 1 
txtemail = driver.find_element(By.XPATH,"//*[@id=\"email\"]")
# cach2 
# txtemail = driver.find_element_by_name("email")
txtpassword = driver.find_element_by_xpath("//*[@id=\"pass\"]")

txtemail.send_keys("abc@gmail.com")
txtpassword.send_keys("123456")  


# btnlogin = driver.find_element_by_name("login")
# btnlogin.click()
# cach viet gon lai
# =========click = name=============
# driver.find_element_by_name("login").click() 
# =========click = xpath=============
driver.find_element_by_xpath("//*[@name=\"login\"]").click() 

time.sleep(5)

txttb=driver.find_element_by_xpath("//*[@role=\"alert\"]").text
print("\n",txttb,"\n")
# driver.close()
