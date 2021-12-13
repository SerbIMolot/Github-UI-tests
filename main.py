from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from assert_custom import *
from selenium_ext import *
from tests import *


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

try:
    searchTest(drive0r,'kiwitcms/Kiwi','kiwitcms/Kiwi')
    searchTest(driver,'Kiwi','kiwitcms/Kiwi', True)
    SignUpFieldsTest(driver, 'testingemail@gmail.com', "asdf1234", "Wtawwwse", "n")
    SignUpFieldsTest(driver, 'testingem**ail@gmail.com', "asdf1234", "Wtawwwse", "n")
    SignUpFieldsTest(driver, 'testingem**ail@gmail.com', "asdf1234", "і", "n")
    SignUpFieldsTest(driver, 'testingemail@gmail.com', "asdf123іівц4", "і1414124222", "n")
except AssertFailed:
    print("Tests failed")
    

driver.quit()
