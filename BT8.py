
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

driver.get("https://courses.letskodeit.com/practice")
# kiem tra co hien ko 
btnhide=driver.find_element_by_id("hide-textbox")
btnshow= driver.find_element_by_id("show-textbox")
txthideshow = driver.find_element_by_id("displayed-text")

print(txthideshow.is_displayed())
btnhide.click()
# ====================================================================
# khi cho ẩn thì thử nhập giá trị vào 
driver.execute_script("arguments[0].value='setHide'",txthideshow)
# driver.execute_script("arguments[0].click()",txthideshow)
# ===================================================================
print(txthideshow.is_displayed())
btnshow.click()
# print(txthideshow.is_displayed())
# # kiem tra co hoat dong khong
# btndisable1= driver.find_element_by_id("disabled-button")
# btnenable1= driver.find_element_by_id("enabled-button")
# txtde1 = driver.find_element_by_id("enabled-example-input")

# print(txtde1.is_enabled())
# btndisable1.click()
# print(txtde1.is_enabled())
# btnenable1.click()
# print(txtde1.is_enabled())

# # kiem tra radio 
# bmw = driver.find_element_by_id("bmwradio")
# # benz = driver.find_element_by_id("benzradio")
# # honda = driver.find_element_by_id("hondaradio")
# if not bmw.is_selected():
#     bmw.click()

# # kiem tra checkbox 
# btnbmw = driver.find_element_by_id("bmwcheck")
# btnbez = driver.find_element_by_id("benzcheck")
# btnhonda = driver.find_element_by_id("hondacheck")
# if not btnbmw.is_selected():
#     btnshow.click()
# if not btnbez.is_selected():
#     btnbez.click()
# if btnhonda.is_selected():
#     btnhonda.click()

# # kiem tra multiple 
# apple = driver.find_element(By.XPATH,"//*[@id=\"multiple-select-example\"]/option[1]")
# orange = driver.find_element(By.XPATH,"//*[@id=\"multiple-select-example\"]/option[2]")
# peach = driver.find_element(By.XPATH,"//*[@id=\"multiple-select-example\"]/option[3]")

# if not apple.is_selected():
#     apple.click()


# # # kiem tra checkbox
# # driver.get("http://the-internet.herokuapp.com/checkboxes")
# # checkbox1 = driver.find_element_by_xpath("//*[@id=\"checkboxes\"]/input[1]")
# # checkbox2 = driver.find_element_by_xpath("//*[@id=\"checkboxes\"]/input[2]")
# # # de: chi chon checkbox1 
# # if not checkbox1.is_selected():
# #     checkbox1.click()
# # if checkbox2.is_selected():
# #     checkbox2.click()
