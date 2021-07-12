from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DriverLogic:

    def __init__(self, driver):
        self.driver = driver

    def ytmLogin(self, ytmName: str, ytmPass: str):
        self.driver.get("https://www.ytmonster.net/login")

        loginName = self.driver.find_element_by_id("inputUsername")
        loginName.clear()
        loginName.send_keys(ytmName)

        loginPass = self.driver.find_element_by_id("inputPassword")
        loginPass.clear()
        loginPass.send_keys(ytmPass)
        loginPass.send_keys(Keys.RETURN)

        print(self.driver.current_url)