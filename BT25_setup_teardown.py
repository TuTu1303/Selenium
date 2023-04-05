from re import T
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from setuptools import setup
import setuptools
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# ======import action chain 
from selenium.webdriver.common.action_chains import ActionChains
# ====================C2====thay thế cho time.sleep================
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ExampleSeleniumTestCase(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        # Giu brower không bị tắT 
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("--log-level=3")

        # Using webdriver_manager to install webdriver automatically
        self.driver= Chrome(service= Service(ChromeDriverManager().install()),chrome_options=chrome_options)

    def tearDown(self) -> None:
        self.driver.quit()
    def test_open_google(self):
        # 1. Open this link 
        self.driver.get("https://www.google.com.vn/?hl=vi")
        self.assertEqual("Google",self.driver.title)
    def test_open_vnexpress(self):
        # 1. Open this link 
        self.driver.get("https://vnexpress.net/")
        # self.assertEqual("https://vnexpress.net/",self.driver.title)

if __name__ == '__main__':
    unittest.main()
    