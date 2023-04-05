from select import select
from unicodedata import name
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
# chi in ra cac truong fail 
Chrome_options.add_argument("--log-level=3")

# Chrome_options.add_argument("user-data-dir=C:\\Users\hv\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# su dung webdriver_manager ti install webdriver tu dong 
driver = Chrome(service = Service(ChromeDriverManager().install()),options=Chrome_options)
# ====================C1====thay thế cho time.sleep================
# Dùng để xét nó tìm đi tìm lại element chứ không cừng dùng time.slep tốn tg 
driver.implicitly_wait(10)

driver.get("https://courses.letskodeit.com/practice")
driver.find_element(By.ID,"opentab").click()
driver.switch_to.window(driver.window_handles[1])
search = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//*[@id='search'])[2]")))
search.send_keys("Testng")
search.submit()

# Lam cho trang web cu bij mat ddi 
# hoac co the dung time. spleep
WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'JavaScript for beginners')]")))

list_name=driver.find_elements(By.XPATH,"//h4[@class='dynamic-heading']")
for item in list_name:
    print(item.text)