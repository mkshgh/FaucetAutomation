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
import webbrowser
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# To do :
# - Recursive Wait
# - Rotate proxies
# http://www.freeproxylists.net/
# Base URL for the company profile page

BASE_URL = "https://web.telegram.org/#/im?p=@"
PROFILE_DIR = 'profile'
LINK_START = "tg://unsafe_url?url="
IMP_DELAY = 10

# path to your profiles
# I assumed that you had a family, Sorry if you don't.
profiles = ['C:\\pyteleclick\\profiles\\ntc','C:\\pyteleclick\\profiles\\ncell','C:\\pyteleclick\\profiles\\dad','C:\\pyteleclick\\profiles\\mom','C:\\pyteleclick\\profiles\\dadncl']
channels = 'Litecoin_click_bot'

# Initialize the driver object
# driver = webdriver.Chrome()

# Load symbols

def get_driver(profile):
    options = FirefoxOptions()
    options.add_argument("--headless")
    fp = webdriver.FirefoxProfile(profile)
    teleminebot = webdriver.Firefox(firefox_profile=fp,options=options)
    return teleminebot

def implicitwait(main_tab,delay=IMP_DELAY):
    """ Implicit wait """
    main_tab.implicitly_wait(delay)

def wait(delay=IMP_DELAY):
    """ Explicit wait """
    time.sleep(delay)

# def get_link(driver):
    
def open_link_in_chrome(money_link,temp_link,view_time,main_tab):
    webbrowser.open(money_link)
    while  money_link==temp_link:
        view_time = view_time+15
        money_link = get_money_link(main_tab)
        print('adding 15s to the loop: '+str(view_time))
        wait(15)
        if view_time>120:
            temp_link=''
            break
    try:
        os.system("taskkill /f /im  Brave.exe >nul 2>&1")
        print('Browser closed'+'\n')
    except:
        pass
    return view_time

def logger(text,money_link,view_time,profile):
    logs_write='['+profile+'] : ' + str(datetime.datetime.now())+ " > " + text + ' '+ str(money_link) + " for "+str(view_time)+'s'
    f.write(logs_write)
    print(logs_write)

def get_money_link(main_tab):
    try:
        # Keep clicking the button forever and make money
        link:str = main_tab.find_element(By.XPATH,"(//a[starts-with(@href, 'tg://unsafe_url?url=')])[last()]").get_attribute("href")
        # Link has unwanted initials and is in UTF-8, So removing those at first
        money_link = str(unquote(link.replace("tg://unsafe_url?url=",'')))
    except:
        money_link='https://dogeclick.com/terms'
    return money_link

def click_visit_site(main_tab):
    try:
        main_tab.find_element(By.XPATH, '//button[contains(text()," Menu")]').click()
        print('Clicking Menu button')
        wait(5)
    except:
        pass
    # Click the button to visit sites
    menu_button = main_tab.find_element(By.XPATH, '//button[contains(text()," Visit sites")]')
    menu_button.click()
    wait(5)

def click_menu_button(main_tab):
    try:
        main_tab.find_elements_by_xpath('//button[@class="btn btn-md" and .//span[contains(., "Cancel")]]').click()
        wait(2)
    except:
        pass
    # click menu button if the menu_button not clicked
    menu_button = main_tab.find_element(By.XPATH, "//a[@id='menubutton']")
    menu_button.click()
    wait(3)

def ads_finished(main_tab):
    last_message = main_tab.find_elements_by_xpath("//div[@class='im_history_messages_peer']/div[@class='im_history_message_wrap']")[-1].get_attribute('innerHTML')
    adsFinished = 'Sorry, there are no new ads available.' in last_message
    return adsFinished

def create_menu_button(main_tab):
    main_tab.execute_script("""
    var menubutton_a = document.createElement('a'); 
    var link = document.createTextNode('menubutton');
    menubutton_a.appendChild(link);
    menubutton_a.id = 'menubutton';
    menubutton_a.href = 'tg://bot_command?command=menu';
    document.body.appendChild(menubutton_a);
    """)
    wait(5)

def runner(profile):
    # get driver to create a main_tab
    main_tab = get_driver(profile)
    profile = profile.split('\\')[-1]
    print('['+profile+ '] : ' +'Getting the browser ready')
    main_tab.get(BASE_URL+channels)
    # wait(main_tab) to load
    # wait for the main_tab to load
    wait()
    # set variables for future use
    print('Setting the variables and Entering the loop')
    view_time=15
    temp_link=''
    stop=1
    create_menu_button(main_tab)
    click_menu_button(main_tab)
    wait(5)

    while stop:
        # click the visit site to get the link
        click_visit_site(main_tab)
        wait(5)

        if ads_finished(main_tab):
            stop = 0
        
        else:
            # links status from the url
            money_link=get_money_link(main_tab)
            view_time = open_link_in_chrome(money_link,temp_link,view_time,main_tab)
            logger('Visit Website',money_link,view_time,profile)
            view_time = 15
            temp_link=money_link

    main_tab.quit()
    wait(1)

if __name__ == "__main__":
    # check if new ads are avialable
    current_crypto_index=0
    while True:     
        f = open("logs.txt", "a+")
        runner(profiles[current_crypto_index])
        current_crypto_index = current_crypto_index+1
        if current_crypto_index == len(profiles):
            current_crypto_index=0
        f.close()
