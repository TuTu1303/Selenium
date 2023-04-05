from select import select
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

# Chrome_options.add_argument("user-data-dir=C:\\Users\hv\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# su dung webdriver_manager ti install webdriver tu dong 
driver = Chrome(service = Service(ChromeDriverManager().install()),options=Chrome_options)
# ====================C1====thay thế cho time.sleep================
# Dùng để xét nó tìm đi tìm lại element chứ không cừng dùng time.slep tốn tg 
driver.implicitly_wait(10)

driver.get("https://www.traveloka.com/vi-vn/")
driver.find_element(By.XPATH,"(//div[contains(text(),'Vận chuyển')])[1]").click()
driver.find_element(By.XPATH,"(//div[contains(text(),'Vé máy bay')])[1]").click()
driver.find_element(By.XPATH,"(//*[@Class='css-1dbjc4n r-1kb76zh'])[1]").click()
driver.find_element(By.XPATH,"//*[contains(text(),'TP HCM, Việt Nam')]").click()
driver.find_element(By.XPATH,"(//*[@Class='css-1dbjc4n r-1kb76zh'])[2]").click()
driver.find_element(By.XPATH,"//*[contains(text(),'Đà Nẵng, Việt Nam')]").click()
driver.find_element(By.XPATH,"(//*[@Class='css-1dbjc4n r-1kb76zh'])[4]").click()
driver.find_element(By.XPATH,"//*[@Class='css-1dbjc4n r-18u37iz']//*[contains(text(),'12')]").click()
driver.find_element(By.XPATH,"//*[@Data-testid='desktop-default-search-button']").click()
for item in range(1,11):
    ten = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//*[@Class='css-901oao r-1sixt3s r-ubezar r-majxgm r-135wba7 r-aq742g r-fdjqy7'])[" + str(item) + "]")))
    tg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//*[@Class='css-1dbjc4n r-obd0qt r-1b7u577']/div[1])[" + str(item) + "]")))
    gia = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//*[@Class='css-1dbjc4n r-1awozwy r-18u37iz r-1w6e6rj r-17s6mgv r-6gpygo']/div[1])[" + str(item) + "]")))
    print(ten.text,"\t",tg.text,"\t",gia.text)
