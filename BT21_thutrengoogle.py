from lib2to3.pgen2 import driver
from turtle import title
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# ======import action chain 
from selenium.webdriver.common.action_chains import ActionChains
# ====================C2====thay thế cho time.sleep================
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class testcaseSample(unittest.TestCase):
    def test_open_google(self):
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

        driver.get("https://www.google.com.vn/?hl=vi")
        self.assertEqual("Google",driver.title)

if __name__ == '__main__':
    unittest.main()
    