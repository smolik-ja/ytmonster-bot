from driver_logic import DriverLogic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driverLogic = DriverLogic(driver)

driverLogic.ytmLogin("name", "pass")