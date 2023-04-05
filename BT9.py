
from select import select
from tkinter.tix import Select
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
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
driver.get("https://courses.letskodeit.com/practice")
select = Select(driver.find_element(By.ID,"carselect"))
time.sleep(5)
select.select_by_value("benz")
time.sleep(5)
# select.select_by_visible_text("Honda")
# time.sleep(5)
# select.select_by_index("0")
