from driver_logic import DriverLogic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driverLogic = DriverLogic(driver)

driverLogic.ytmLogin("name", "pass")