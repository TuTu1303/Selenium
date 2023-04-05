
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(service = Service(ChromeDriverManager().install()))

driver.get("http://automationpractice.com/index.php")
driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/nav/div[1]/a").click()
driver.find_element(By.LINK_TEXT,"Forgot your password?").click()
time.sleep(5)