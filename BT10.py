
from select import select
from tkinter.tix import Select
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#chrome option
Chrome_options = Options()
# giu chrome ko bi tat 
Chrome_options.add_experimental_option("detach",True)
# su dung webdriver_manager ti install webdriver tu dong 
driver = Chrome(service = Service(ChromeDriverManager().install()),options=Chrome_options)
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/courses")
driver.find_element(By.XPATH,"(//*[@Class='btn-group'])[1]/button").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Software Testing')]").click()
# time.sleep(2)
driver.find_element(By.XPATH,"(//*[@Class='btn-group'])[2]/button").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Hemil Patel')]").click()
# time.sleep(2)
list_hemil = driver.find_elements(By.XPATH,"//*[@Class='course-listing-title']")
for item in list_hemil:
    print(item.text)