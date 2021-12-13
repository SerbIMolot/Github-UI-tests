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

def CSS_ClassCBtnlick( driver, css_selector, action_name):
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        button.click()   
    except TimeoutException:
        print(action_name + " failed")
        return False
    print(action_name + " passed")
    return True

def Send_Keys_On_Visibility( driver, waitTime, by, msg, selector):
    emailField = WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((by, selector)))
    emailField.clear()
    emailField.send_keys(msg)


