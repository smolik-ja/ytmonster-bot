from constants import Constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pickle

class DriverLogic:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # hides WebDriver window
        # options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    def closeWebDriver(self):
        self.driver.close()

    # def ytmLogin(self, ytmName: str, ytmPass: str):
    #     self.driver.get("https://www.ytmonster.net/login")

    #     loginName = self.driver.find_element_by_id("inputUsername")
    #     loginName.clear()
    #     loginName.send_keys(ytmName)

    #     loginPass = self.driver.find_element_by_id("inputPassword")
    #     loginPass.clear()
    #     loginPass.send_keys(ytmPass)
    #     loginPass.send_keys(Keys.RETURN)

    #     print(self.driver.current_url)

    def ytmLogin(self):
        logged = False
        self.driver.get(Constants().ytmLoginLink)

        while (logged == False):
            if self.driver.current_url == Constants().ytmDashboardLink:
                logged = True
                pickle.dump(self.driver.get_cookies(),open(Constants().cookiesName,"wb"))

        print(self.driver.current_url)
        self.driver.close()

    def openYtm(self):
        self.driver.get(Constants().ytmLoginLink)
        cookies = pickle.load(open(Constants().cookiesName, "rb"))
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)
        self.driver.get(Constants().ytmDashboardLink)