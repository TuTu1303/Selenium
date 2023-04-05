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

class ExampleSeleniumTestCase1(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        # Giu brower không bị tắT 
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("--log-level=3")

        # Using webdriver_manager to install webdriver automatically
        self.driver= Chrome(service= Service(ChromeDriverManager().install()),chrome_options=chrome_options)

    # def tearDown(self) -> None:
    #     self.driver.quit()
    # def test_case1(self):
    #     # 1. Open this link 
    #     self.driver.get("http://automationpractice.com/index.php")
    #     self.driver.maximize_window()
    #     self.driver.find_element(By.CLASS_NAME,"login").click()
    #     self.driver.find_element(By.ID,"email").send_keys("nga.tran+++++1@hdwebsoft.io")
    #     self.driver.find_element(By.ID,"passwd").send_keys("Nga@123")
    #     self.driver.find_element(By.ID,"SubmitLogin").click()
    #     a= self.driver.find_element(By.ID,"search_query_top")
    #     a.send_keys("Summer")
    #     a.submit()
    #     self.driver.find_element(By.ID,"grid").click()

    #     item = self.driver.find_element(By.XPATH,"(//h5[@itemprop='name']/a)[1]")
    #     action= ActionChains(self.driver)
    #     action.move_to_element(item)
    #     action.perform()

    #     adtocart = self.driver.find_element(By.XPATH,"(//span[contains(text(),'Add to cart')])[1]")
    #     print(adtocart.is_displayed())
    #     more = self.driver.find_element(By.XPATH,"(//span[contains(text(),'More')])[1]")
    #     print(more.is_displayed())

    def test_case2(self):
        # 1. Open this link 
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Contact us')]").click()
        self.driver.find_element(By.ID,"email").send_keys("yennga2812@gmail.com")
        self.driver.find_element(By.ID,"id_order").send_keys("123")
        self.driver.find_element(By.ID,"fileUpload").send_keys("SampleTestcase.txt")
        Select(self.driver.find_element(By.ID,"id_contact")).select_by_value("2")

        self.driver.find_element(By.ID,"message").send_keys("trsfhaskjfhdsjkfhaskjldghkjsadhgaskjhgjlkadshglkjadhgjkladhgjksdhb")
        self.driver.find_element(By.ID,"submitMessage").click()
        print()
if __name__ == '__main__':
    unittest.main()
    