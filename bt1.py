from selenium.webdriver import Chrome
driver = Chrome(executable_path="./chromedriver.exe")

def verifyText(text1, text2):
    if text1 == text2:
        print("True")
    else:
        print("False")

driver.get("https://www.selenium.dev/")
verifyText(driver.title,"SeleniumHQ Browser Automation")
driver.get("https://www.python.org/")
verifyText(driver.title,"Python.org")
driver.back()
verifyText(driver.title,"SeleniumHQ")
driver.forward()
verifyText(driver.title,"Welcome to Python.org")
