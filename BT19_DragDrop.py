from argparse import Action
from inspect import isframe
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

# ======import action chain 
from selenium.webdriver.common.action_chains import ActionChains
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
# driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
time.sleep(2)

# begin= driver.find_element(By.ID,"fourth")
# end = driver.find_element(By.CLASS_NAME,"ui-widget-content")

# action = ActionChains(driver)
# action.drag_and_drop(begin,end)
# action.perform()

isframeytest = driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(isframeytest)

end = driver.find_element(By.ID,"trash")
action = ActionChains(driver)

for item in range(1,5):
    
    begin= WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//*[@id='gallery']/li)[" + str(item) + "]")))
    action.drag_and_drop(begin,end)
    action.perform()
    time.sleep(1)