from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#chrome option
Chrome_options = Options()
# giu chrome ko bi tat 
Chrome_options.add_experimental_option("detach",True)
# su dung webdriver_manager ti install webdriver tu dong 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = Chrome(service = Service(ChromeDriverManager().install()),options=Chrome_options)

driver.get("https://vi-vn.facebook.com/")
txtemail= driver.find_element_by_id("email")
txtpassword = driver.find_element_by_id("passContainer")

# is_displayed() hien tren man hinh
print(txtemail.is_displayed())
print(txtpassword.is_displayed())
# is_enabled() the hien co the tuong tac duoc tren man hinh
print(txtemail.is_enabled())
print(txtpassword.is_enabled()) 