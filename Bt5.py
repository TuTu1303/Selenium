
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = Chrome(service = Service(ChromeDriverManager().install()))

driver.get("https://cellphones.com.vn/")
txtsearch=driver.find_element(By.ID,"search")
txtsearch.send_keys("iphone")
# txtsearch.send_key(Keys.ENTER)
txtsearch.submit()
driver.find_element(By.XPATH,"//*[@Class= 'item-product'][1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@Onclick= 'addToCart()']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@Class= 'btn-submit mt-2']//a").click()

txtsearch=driver.find_element(By.ID,"search")
txtsearch.send_keys("iphone")
txtsearch.submit()
driver.find_element(By.XPATH,"//*[@Class= 'item-product'][2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@Onclick= 'addToCart()']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@Class= 'btn-submit mt-2']//a").click()

txtsearch=driver.find_element(By.ID,"search")
txtsearch.send_keys("iphone")
txtsearch.submit()
driver.find_element(By.XPATH,"//*[@Class= 'item-product'][3]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@Onclick= 'addToCart()']").click()
time.sleep(10)
list_cart = driver.find_elements(By.XPATH,"//*[@Class='product-name']")
# print(list_cart.text)
count = 0
for item in list_cart:
    print(item.text)
    count+=1
print(count)
time.sleep(30)