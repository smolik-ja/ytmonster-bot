from constants import Constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pickle

class DriverLogic:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # hides WebDriver window
        options.headless = False
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
                print(self.driver.get_cookies())
                pickle.dump(self.driver.get_cookies(),open(Constants().ytmCookies,"wb"))

        print(self.driver.current_url)
        self.driver.close()

    def openYtm(self):
        self.driver.get(Constants().ytmLoginLink)
        cookies = pickle.load(open(Constants().ytmCookies, "rb"))
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(Constants().ytmDashboardLink)

    def ytLogin(self, login, pwd):
        logged = False
        self.driver.get(Constants().ytLoginLink)

        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button').click()
        self.driver.find_element_by_id("identifierId").send_keys(login)
        self.driver.find_element_by_name("password").send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()


        while (logged == False):
            if self.driver.current_url == "https://www.youtube.com/":
                logged = True
                print(self.driver.get_cookies())
                pickle.dump(self.driver.get_cookies(),open(Constants().ytCookies,"wb"))

        print(self.driver.current_url)
        self.driver.close()

    def openYt(self):
        self.driver.get(Constants().ytLoginLink)
        cookies = pickle.load(open(Constants().ytCookies, "rb"))
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://www.youtube.com/")