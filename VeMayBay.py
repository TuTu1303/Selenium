from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Chrome option 
chrome_options = Options()
# Giu browser khong bi tat
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-data-dir=C:\\Users\hv\\AppData\\Local\\Google\\Chrome\\User Data\\Default")


#Using webdriver_manager to install webdriver automatically
driver = Chrome(service=Service(ChromeDriverManager().install()), options= chrome_options)
driver.maximize_window()

# 1. Open this link http://automationpractice.com/index.php
driver.get("https://www.traveloka.com/vi-vn/")
