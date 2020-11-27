
##### selenium_functions.py
#####   This file contains all Selenium functions used in the entire project.

import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


#####    Due to the site's rights, I cannot share with you guys the full searching algorithm.
#####  Instead, I encourage to have a look on a video that's presenting how this application works in a real time.
#####  Have a nice day!

PROPER_FIGHTER_URL_PREFACE = ""

def find_elements(xpath):
    global driver
    return driver.find_elements_by_xpath(xpath)

def fill_entry(xpath, content):
    global driver
    WebDriverWait(driver, 40).until(Ec.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).send_keys(content)

def click_element(xpath):
    global driver
    WebDriverWait(driver, 40).until(Ec.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).click()

def click_enter(repeat=1):
    global driver
    ActionChains(driver).send_keys(Keys.ENTER*repeat).perform()

def get_text(xpath):
    global driver
    return driver.find_element_by_xpath(xpath).text

def get_photo(xpath, filename):
    global driver
    return driver.find_element_by_xpath(xpath).screenshot(filename=filename)

def close_driver():
    try:
        global driver
        driver.close()
    except Exception as e:
        print("Sir, something went wrong with closing driver: \n", e)


def run_driver(url=None, fighter_name=None, headless=False) -> "runs driver":
    """
    Start Selenium based on passed arguments:
        a) url           -> directly into certain page
        b) fighter_name  -> take some seconds to find a page ;)
    """

    # global driver
    # if headless:
    #     options = Options()
    #     options.add_argument("--headless")
    #     driver = webdriver.Chrome(executable_path='Selenium\chromedriver.exe', options=options)
    # else:
    #     driver = webdriver.Chrome(executable_path='Selenium\chromedriver.exe')
    #     driver.minimize_window()
    #
    # if url:
    #     driver.get(url)
    #     return
    #
    # if fighter_name:
        # driver.get(
        #     url=''
        # )
        # fill_entry(
        #     xpath='',
        #     content='',
        # )
        # ...
    pass


def grab_fighter_info() -> "returns 2 lists":
    """
    Get all necessary informations about fighter and return them as 2 lists:
        first   -> info
        second  -> career history (fights)
    """

    fighter_info_list = []
    fighter_career_history = []

    ##################### GENERAL INFO
    ##### ACCEPT COOKIES

    ##### NAME / ALIAS

    ##### NATIONALITY / CITY / AFFILIATION

    ##### BORN / AGE / HEIGHT / WEIGHT

    ##### PHOTO / FLAG


    ##################### UPCOMING FIGHT

    ##################### STATS
    ##### WINS

    ##### LOSSES

    ##### DRAWS

    ##### TOTAL AMOUNT OF FIGHTS

    ##### RECENT FIGHT

    ##### FIRST FIGHT

    ##### YEARS OF PROFESSIONAL MMA CAREER


    ##################### MMA RECORD


    ##################### CAREER HISTORY


    ##################### LAST STREAK


    ##################### SUMMING UP


    ##################### CLOSE DB


    ################### RETURN 2 LISTS FULL OF INFORMATIONS
    return fighter_info_list, fighter_career_history
