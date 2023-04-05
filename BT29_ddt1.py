import unittest
from ddt import ddt,unpack,data

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
from selenium.common.exceptions import TimeoutException


@ddt
class DDTSample(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        # Giu brower không bị tắT 
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("--log-level=3")

        # Using webdriver_manager to install webdriver automatically
        self.driver= Chrome(service= Service(ChromeDriverManager().install()),chrome_options=chrome_options)

    
    def tearDown(self) -> None:
        print("My Teardown")
        # self.driver.quit()

    @data(["test12222@lo.com","12345678"],["test12223@lo.com","12345678"],["test12224@lo.com","12345678"])
    @unpack
    def test_case1(self,value1,value2):
        # 1. Open this link 
        self.driver.get("http://automationpractice.com/")
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Sign in')]").click()
        self.driver.find_element(By.ID,"email").send_keys(value1)
        self.driver.find_element(By.ID,"passwd").send_keys(value2)
        self.driver.find_element(By.ID,"SubmitLogin").click()
        thongbao=self.driver.find_element(By.XPATH,"//li[contains(text(),'Authentication failed.')]").text
        self.assertTrue(thongbao.is_displayed())
        # print(thongbao)
        # self.assertEqual("Authentication failed.",thongbao)
        # try:
        #     WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//li[contains(text(),'Authentication failed.')]")))
        # except TimeoutException:
        #     self.fail("No error message appear")

    # @data(3,5,7,9,10)
    # def test_is_prime(self,value):
    #     print(value)
    #     self.assertTrue(is_prime(value))

    # @data([1,2,3],[2,3,5],[5,6,11])
    # @unpack
    # def test_plus(self,value1,value2,value3):
    #     self.assertEqual(plus(value1,value2),value3)

    # @data([9,3,3],[5,5,1],[7,8,9])
    # @unpack
    # def test_divide(self,value1,value2,value3):
    #     self.assertEqual(divide(value1,value2),value3)

if __name__ == '__main__':
    unittest.main()
    