from assert_custom import *
from selenium_ext import *

def searchTest(driver, find_str, exp_str, expect_to_fail = False):
    searchBar = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'form-control.input-sm.header-search-input.jump-to-field.js-jump-to-field.js-site-search-focus')))

    searchBar.clear()
    searchBar.send_keys(find_str)
    searchBar.send_keys(Keys.ENTER)

    firstResult = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#js-pjax-container > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > ul > li:nth-child(1) > div.mt-n1.flex-auto > div.d-flex > div.f4.text-normal > a')))
    # result = firstResult.get_attribute('href')
    result = firstResult.text

    AssertTest(exp_str, result, expect_to_fail)

#Imposible to finish because of test on human
def SignUpFieldsTest(driver, email, password, username, updates):
    driver.get("https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home")

    Send_Keys_On_Visibility(driver, 20, By.ID, email, 'email')
    
    success = CSS_ClassCBtnlick(driver, '#email-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button', 'Email')

    AssertTrue(success, "Email")

    Send_Keys_On_Visibility(driver, 20, By.ID, password, 'password')
    success = CSS_ClassCBtnlick(driver,  '#password-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button', "Password")

    AssertTrue(success, "password")

    Send_Keys_On_Visibility(driver, 20, By.ID, username, 'username')
    success = CSS_ClassCBtnlick(driver,  '#username-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button', "Username")

    AssertTrue(success, "username")
    
    Send_Keys_On_Visibility(driver, 20, By.ID, updates, 'opt_in')
    success = CSS_ClassCBtnlick(driver, '#opt-in-container > div.d-flex.flex-items-center.flex-column.flex-sm-row > button', "Updates")

    AssertTrue(success, "opt_in")