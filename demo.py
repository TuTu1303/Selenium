# Chrome
# from selenium.webdriver import Chrome
# driver = Chrome(executable_path="./chromedriver.exe")
# driver.maximize_window()

# Firefox
# from selenium.webdriver import Firefox
# driver = Firefox(executable_path="geckodriver.exe")

#edge
# from selenium.webdriver import Edge
# driver = Edge(executable_path="msedgedriver.exe")
# driver.maximize_window()
# driver.get("https://www.youtube.com/")
# print(driver.current_url)
# # print(driver.page_source)
# print(driver.title)


from matplotlib.pyplot import text
from selenium.webdriver import Chrome

def verifyText(text1, text2):
    if text1 == text2:
        print("True")
    else:
        print("False")


driver = Chrome(executable_path="./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/")
print(driver.title)
driver.get("https://www.google.com.vn/")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)


verifyText(driver.title,"abc")
