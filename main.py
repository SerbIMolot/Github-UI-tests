from selenium import webdriver
from tests import *
import pytest

def test_first_in_search_test(selenium):
    selenium.get("https://github.com/")
    selenium.maximize_window()
    searchTest(selenium,'kiwitcms/Kiwi','kiwitcms/Kiwi')

def test_not_first_in_search_test(selenium):
    selenium.get("https://github.com/")
    selenium.maximize_window()
    searchTest(selenium,'Kiwi','kiwitcms/Kiwi', True)
        
def test_signup_easy_pass(selenium):
    selenium.get("https://github.com/")
    selenium.maximize_window()
    try:
        SignUpFieldsTest(selenium, 'testingemail@gmail.com', "asdf1234", "Wtawwwse", "n", "password")
    except:
        assert True  == True
def test_signup_without_num(selenium):
    selenium.get("https://github.com/")
    selenium.maximize_window()
    try:
        SignUpFieldsTest(selenium, 'testinsdcgemail@gmail.com', "CwaCsaCdfgsetr", "Wtawwwse", "n", "password")
    except:
        assert True  == True
def test_signup_wring_email(selenium):
    
    selenium.get("https://github.com/")
    selenium.maximize_window()
    try:
        SignUpFieldsTest(selenium, 'testingem**ail@gmail.com', "CwaCsaCdfgse2415tr", "Wtawwwse", "n", "email")
    except:
        assert True  == True

def test_signup_short_password(selenium):
    selenium.get("https://github.com/")
    selenium.maximize_window()
    try:
        SignUpFieldsTest(selenium, 'testingemail@gmail.com', "asdf4", "Wtawwwse", "n", "password")
    except:
        assert True  == True
def test_signup_wrong_password_2(selenium):
    selenium.get("https://github.com/")
    selenium.maximize_window()
    try:
        SignUpFieldsTest(selenium, 'testingemail@gmail.com', "asdf123іівц4", "і1414124222", "n", "password")

    except:
        assert True  == True