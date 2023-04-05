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

        driver.get("http://automationpractice.com/index.php")
        driver.find_element(By.CLASS_NAME,"login").click()
        driver.find_element(By.ID,"email").send_keys("nga.tran+++++1@hdwebsoft.io")
        driver.find_element(By.ID,"passwd").send_keys("Nga@123")
        driver.find_element(By.ID,"SubmitLogin").click()
        a= driver.find_element(By.ID,"search_query_top")
        a.send_keys("Summer")
        a.submit()
        driver.find_element(By.ID,"grid").click()
        driver.find_element(By.XPATH,"(//*[@class='product-container'])[1]").click()
        c= driver.find_element(By.XPATH,"//h1[contains(text(),'Printed Summer Dres')]").text
        self.assertEqual("Printed Summer Press",c)

        black = driver.find_element(By.ID,"color_11")
        orange = driver.find_element(By.ID,"color_13")
        blue = driver.find_element(By.ID,"color_14")
        yellow = driver.find_element(By.ID,"color_16")

if __name__ == '__main__':
    unittest.main()
    