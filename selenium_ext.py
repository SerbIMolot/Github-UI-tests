from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium_ext import *
import pytest

MAX_ELEMENT_WAIT_TIME = 10

def CSS_ClassCBtnlick( driver, css_selector, action_name, expect=False):
    try:
        if(expect==True):
            with pytest.raises(selenium.common.exceptions.TimeoutException) as e_info:
                button = WebDriverWait(driver, MAX_ELEMENT_WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
                button.click()
        else:    
            button = WebDriverWait(driver, MAX_ELEMENT_WAIT_TIME).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
            button.click()
    except selenium.common.exceptions.TimeoutException:
        print(action_name + " failed")
        return False
    finally:
        print(action_name + " passed")
        return True

    print(action_name + " passed")
    return True

def Send_Keys_On_Visibility( driver, by, msg, selector,expect = False):
    if(expect==True):
        with pytest.raises(selenium.common.exceptions.TimeoutException) as e_info:
            emailField = WebDriverWait(driver, MAX_ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located((by, selector)))
            emailField.clear()
            emailField.send_keys(msg)
    else:    
        emailField = WebDriverWait(driver, MAX_ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located((by, selector)))
        emailField.clear()
        emailField.send_keys(msg)



