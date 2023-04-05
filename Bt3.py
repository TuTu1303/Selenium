# from lib2to3.pgen2 import driver
# from pandas import array
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# import time
# driver = Chrome(executable_path="./chromedriver.exe")
# =============cho selenium 3.7 tro len 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(service = Service(ChromeDriverManager().install()))


driver.get("http://automationpractice.com/index.php")
driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/nav/div[1]/a").click()
driver.find_element_by_id("email").send_keys("test28@gmail.com")
driver.find_element_by_id("passwd").send_keys("12345678")
driver.find_element_by_id("SubmitLogin").click()
driver.find_element_by_xpath("//*[@id=\"center_column\"]/div/div[1]/ul/li[4]/a").click()
# lay value dung .get_attribute("value")
txtemail = driver.find_element_by_id("email").get_attribute("value")
print(txtemail)

driver.find_element_by_xpath("//*[@id=\"block_top_menu\"]/ul/li[1]/a").click()
# in ra danh sach ten sp 
arr = driver.find_elements_by_xpath("//*[@class=\"product-name\"]")
for item in arr:
    print(item.text)

# in ra ten account 
account=driver.find_element(By.CLASS_NAME,"account").text
print(account)
# cach2
print(driver.find_element_by_xpath("//*[@class='header_user_info']//span").text)

