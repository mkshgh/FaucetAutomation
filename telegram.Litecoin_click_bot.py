"""
Auto telegram Crytominer
Use forever and doesn't detect as a bot
"""
from typing import Any
from selenium import webdriver
from urllib.parse import unquote
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import datetime

# To do :
# - Recursive Wait
# - Rotate proxies
# Go to the following link to signup
# https://t.me/Litecoin_click_bot?start=SnMzz 

BASE_URL = "https://web.telegram.org/#/im?p=@Litecoin_click_bot"
PROFILE_DIR = 'profile'
LINK_START = "tg://unsafe_url?url="
IMP_DELAY = 10

# Add driver to path
# os.environ["PATH"] += os.pathsep + r'driver'

# Create Driver Template
def get_driver():
    # chrome_options = webdriver.ChromeOptions()
    # # chrome_options.add_argument("--headless")
    # a_driver = webdriver.Chrome(options=chrome_options)
    # Use profile in the firefox to store the passwords
    fp = webdriver.FirefoxProfile(PROFILE_DIR)
    teleminebot = webdriver.Firefox(firefox_profile=fp)
    return teleminebot

def wait(delay=IMP_DELAY):
    """ Explicit wait """
    time.sleep(delay)

# def get_link(driver):
    
def open_link_in_chrome(link,delay=35):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/Chrome.exe %s'
    webbrowser.get(chrome_path).open(link)

def logger(text,money_link,view_time):
    logs_write=str(datetime.datetime.now())+ " > " + str(money_link) + " for "+str(view_time)+'s'
    f = open("logs.txt", "a+")
    f.write(logs_write+'\ndescription:'+text+'\n')
    f.close()
    print(logs_write+'\ndescription:'+text+'\n')


def runner():
    # get driver to create a main_tab
    main_tab = get_driver()
    print('Getting the browser ready')
    main_tab.get(BASE_URL)
    

    # wait for the main_tab to load
    # wait(main_tab)
    wait()
    try:
        menu_button = main_tab.find_element(By.XPATH, '//button[contains(text()," Menu")]')
        menu_button.click()
        print('Clicking Menu button')
        wait(5)
    except:
        print('Go directly to the page')
        wait(5)

    view_time=23
    temp_link=''
    print('Entering the loop')
    while True:
        try:
            menu_button = main_tab.find_element(By.XPATH, '//button[contains(text()," Menu")]')
            menu_button.click()
            print('Clicking Menu button')
            wait(5)
        except:
            pass
        
        try:
            # Click the button to visit sites
            menu_button = main_tab.find_element(By.XPATH, '//button[text()="🖥 Visit sites"]')
            menu_button.click()
            # Keep clicking the button forever and make money
            link:str = main_tab.find_element(By.XPATH,"(//a[starts-with(@href, 'tg://unsafe_url?url=')])[last()]").get_attribute("href")
            # Link has unwanted initials and is in UTF-8, So removing those at first
            money_link = str(unquote(link.replace("tg://unsafe_url?url=",'')))
        except:
            money_link='https://dogeclick.com/terms'

        # links status
        wait(5)

        f = open("logs.txt", "a+")

        if view_time>100:
            temp_link=''
            view_time=30
            logger('in a loop here',money_link,view_time)

        elif money_link=='https://dogeclick.com/terms':
            logger(f'That Dogecoin Terms Page: wait for {str(view_time+100)} now, This takes so f#@$ing long.',money_link,view_time+100)
            wait(100)
            temp_link=''
            view_time=30

        elif money_link==temp_link:
            view_time=view_time + 23
            logger('adding 23s to the loop',money_link,view_time)
            open_link_in_chrome(money_link)
            wait(view_time+5)
        
        else:
            temp_link=money_link
            logger('We might be making money',money_link,view_time+5)
            open_link_in_chrome(money_link)
            wait(view_time+5)
    f.close()
    time.sleep(60)
    main_tab.quit()

if __name__ == "__main__":
    runner()