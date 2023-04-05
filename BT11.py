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
# ====================C2====thay thế cho time.sleep================
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#chrome option
Chrome_options = Options()
# giu chrome ko bi tat 
Chrome_options.add_experimental_option("detach",True)
# su dung webdriver_manager ti install webdriver tu dong 
driver = Chrome(service = Service(ChromeDriverManager().install()),options=Chrome_options)
# ====================C1====thay thế cho time.sleep================
# Dùng để xét nó tìm đi tìm lại element chứ không cừng dùng time.slep tốn tg 
# driver.implicitly_wait(10)


driver.get("http://automationpractice.com/index.php")
driver.find_element(By.CLASS_NAME,'login').click()
driver.find_element(By.ID,"email_create").send_keys("nga.tran+++++1@hdwebsoft.io")
driver.find_element(By.ID,'SubmitCreate').click()
# time.sleep(5)
# ====================C2====thay thế cho time.sleep================
gioitinh = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"id_gender2")))
# gioitinh= driver.find_element(By.ID,"id_gender2")
# time.sleep(2)
if not gioitinh.is_selected():
    gioitinh.click()
driver.find_element(By.ID,"customer_firstname").send_keys("TRAN")
driver.find_element(By.ID,"customer_lastname").send_keys("NGA")
driver.find_element(By.ID,"passwd").send_keys("Nga@123")
a=driver.find_element(By.ID,"newsletter")
b=driver.find_element(By.ID,"optin")
if not a.is_selected():
    a.click()
if not b.is_selected():
    b.click()
driver.find_element(By.ID,"firstname").send_keys("TRAN")
driver.find_element(By.ID,"lastname").send_keys("NGA")
driver.find_element(By.ID,"address1").send_keys("89/8,duong 12 khu pho 2 phuong hiep binh chanh ")
driver.find_element(By.ID,"city").send_keys("hhhhh")
select =Select(driver.find_element(By.ID,"id_state"))
select.select_by_value("28")
driver.find_element(By.ID,"postcode").send_keys("00000")
select1 =Select(driver.find_element(By.ID,"id_country"))
select1.select_by_value("21")
driver.find_element(By.ID,"phone_mobile").send_keys("0565789754")
driver.find_element(By.ID,"submitAccount").click()