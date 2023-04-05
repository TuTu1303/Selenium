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


driver.get("https://tiki.vn/")
driver.maximize_window()

# list_voucher = driver.find_elements_by_xpath("//*[@Class='item']//span")
list_voucher = driver.find_elements_by_xpath("//*[@data-view-id='home_quicklinks_tab_container']/a/span")
print(len(list_voucher))
for item in list_voucher:
    # scroll man hinh den vi tri..
    # item.location_once_scrolled_into_view
    print(item.text)
