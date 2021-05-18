"""
Auto telegram Crytominer
"""
from typing import Any
from selenium import webdriver
from urllib.parse import unquote
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# To do :
# - Multiple stakecube Accounts at once
# - Rotate proxies

BASE_URL = "https://stakecube.net/app/community/faucets"
PROFILE_DIR = 'profile'
IMP_DELAY = 20

# Add driver to path
# os.environ["PATH"] += os.pathsep + r'driver'

# Initialize the driver object
# driver = webdriver.Chrome()

# Load symbols


def get_driver():
    # chrome_options = webdriver.ChromeOptions()
    # # chrome_options.add_argument("--headless")
    # a_driver = webdriver.Chrome(options=chrome_options)
    fp = webdriver.FirefoxProfile(PROFILE_DIR)
    fp.set_preference("general.useragent.override", "wanderer-brother")
    teleminebot = webdriver.Firefox(firefox_profile=fp)
    teleminebot.maximize_window()
    return teleminebot

def implicitwait(main_tab,delay=IMP_DELAY):
    """ Implicit wait """
    main_tab.implicitly_wait(delay)

def wait(delay=IMP_DELAY):
    """ Explicit wait """
    time.sleep(delay)

# def get_link(driver):
    

def runner():
    # get driver to create a main_tab
    main_tab = get_driver()
    main_tab.get(BASE_URL)
    

    # wait for the main_tab to load
    # wait(main_tab)
    print('waiting')
    time.sleep(120)
    isnotloop = True 
    claimed_cryptos=0
    while isnotloop:
        # Click the button to visit sites
        time.sleep(15)
        claim_buttons = main_tab.find_elements(By.XPATH, '//button[text()="Claim"]')

        if not claim_buttons:
            print('No claims found')
            main_tab.refresh()

        else:
            for claims in claim_buttons:
                claimed_cryptos=claimed_cryptos+1
                claims.click()
                print('claimed_cryptos:',claimed_cryptos)
                time.sleep(5)  
            main_tab.refresh()
            

        # for claims in claim_buttons:
        #     print(claims.text)
        
        time.sleep(5)

    time.sleep(60)
    main_tab.quit()

if __name__ == "__main__":
    runner()