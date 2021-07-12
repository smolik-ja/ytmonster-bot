from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class DriverLogic:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # hides WebDriver window
        # options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    def closeWebDriver(self):
        self.driver.close()

    def ytmLogin(self, ytmName: str, ytmPass: str):
        self.driver.get("https://www.ytmonster.net/login")

        loginName = self.driver.find_element_by_id("inputUsername")
        loginName.clear()
        loginName.send_keys(ytmName)

        loginPass = self.driver.find_element_by_id("inputPassword")
        loginPass.clear()
        loginPass.send_keys(ytmPass)
        loginPass.send_keys(Keys.RETURN)