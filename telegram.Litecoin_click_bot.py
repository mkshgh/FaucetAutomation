"""
Auto telegram LTC mining BOT
"""
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
import webbrowser
import datetime
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from glob import glob
from subprocess import Popen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

""" Not used now """
# from fake_useragent import UserAgent
# from urllib.parse import unquote
# from typing import Any
# import requests
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import keyboard
# from keyboard import press
# press('enter')
# to remove the popup if exists


# To do :
# - Message the bots
# - Join the channels bots
# channels = 'Litecoin_click_bot'

# Global Variables
CURRENT_DIR = os.getcwd()
BASE_URL = "https://web.telegram.org/z/"
# put all the profile in the profiles folder
PROFILE_DIR = 'C:\\pyteleclick\\profiles\\'
LINK_START = "tg://unsafe_url?url="
IMP_DELAY = 10
profiles = glob(PROFILE_DIR+'/*/')


# Initialize the driver object
def get_driver(profile):
    """ 
    Description: New Instance of the webbrowser with given profile
    Input: 
        profile: <current profile instance>
    Output:
        Instance of the new browser
    """  
    options = FirefoxOptions()
    options.add_argument("--headless")
    fp = webdriver.FirefoxProfile(profile)
    teleminebot = webdriver.Firefox(firefox_profile=fp,options=options)
    teleminebot.maximize_window()
    return teleminebot

def wait(delay=IMP_DELAY):
    """ Implicitly wait """
    time.sleep(delay)

def open_link_in_chrome(money_link,temp_link,main_tab):
    """ 
    Description: open the link in the new browser, since opening in the selenium causes it to track as a bot
    Input: 
        money_link: current money link
        temp_link: previous money link
        main_tab<current tab instance>
    Output:
        link is openeed in the default browser of your manchine.
        I use the Brave so, Brave.exe is closed here.
    """  
    view_time = 0
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
        print('Browser closed')
    except:
        pass
    return view_time

def logger(text,money_link,view_time,profile):
    """ 
    Description: Log the important things
    Input: 
        text: Title of the log
        money_link: current money link
        view_time: The duration of time it ran
        profile: <current profile instance>
    Output:
        The log is written in logs.txt
    """ 
    current_time = datetime.datetime.now()
    logs_time = "{}_{}_{}".format(str(current_time.year),str(current_time.month),str(current_time.day))
    logs_file = os.path.join('logs',(logs_time+"_logs.txt")) 
    f = open(logs_file, "a+")
    logs_write='['+profile+'] : ' + str(datetime.datetime.now())+ " > " + text + ' '+ str(money_link) + " for "+str(view_time)+'s\n'
    f.write(logs_write)
    f.close()
    print(logs_write)

def get_money_link(main_tab):
    """ 
    Description: Get the link to browser
    Input: 
        main_tab: <current tab instance>
    Output:
        link to browse
    """ 
    # Keep clicking the button forever and make money
    main_tab.find_element(By.XPATH,'(//button[text()="🔎 Go to website"])[last()]').click()
    wait(2)
    money_link:str = main_tab.find_element(By.XPATH,'(//div[@class="modal-content custom-scroll"])[last()]/a').get_attribute("href")
    ActionChains(main_tab).send_keys(Keys.ESCAPE).perform()
    wait(1)
    return money_link


def click_the_channel(main_tab):
    """ 
    Description: Click the LTC Click Bot channel
    Input: 
        main_tab: <current tab instance>
    Output:
        Go to the channel
    """
    main_tab.main_tab.find_element(By.XPATH,'//div[@class= "scroll-container"]//h3[text() ="LTC Click Bot"]/../../../..').click()
    wait(2)
    
def ads_status(main_tab):
    """ 
    Description: Status of the ad after clicking the Visit Page button
    Input:
        main_tab: <current tab instance>
    Output:
        the status of the ad: 'nomoreads','visitwebsitenow','usedbyothers',etc
    """
    last_message = main_tab.find_element(By.XPATH,"(//div[@class='message-date-group'][2]/div)[last()]").get_attribute('innerHTML')
    not_loaded = 1
    while not_loaded:
        try:
            if ('Sorry, there are no new ads available.' in last_message):
                return "nomoreads"
                print('No more ads')
            if ('Go to website' in last_message):
                return "visitwebsitenow"
                print('Visit sites now')
            if ('Visit sites' in last_message):
                print('wait 5s until the ads load')
                wait(5)
                last_message = main_tab.find_element(By.XPATH,"(//div[@class='message-date-group'][2]/div)[last()]").get_attribute('innerHTML')
            else:
                return 'usedbyothers'
        except:
            pass
    return 1

def page_loaded(main_tab):
    """ 
    Description: Check if the main page of the telegram is loaded, if not keep waiting
    Input: 
        main_tab: <current tab instance>
    Output:
        fully loaded page
    """
    not_loaded = 1
    view_time=0
    while not_loaded:
        view_time=view_time+10
        if view_time>60:
            view_time=0
            main_tab.refresh()
        try:
            main_tab.find_element(By.XPATH,'//div[@class= "scroll-container"]//h3[text() ="LTC Click Bot"]/../../../..').click()
            wait(5)
            not_loaded=0
        except:
            print('Waiting 5 seconds more until page loads')
            wait(5)
    print('page loaded now')

def clear_cache():
    p = Popen("freeTemp.bat", cwd=r"C:\\pyteleclick\\")


def click_visit_site(main_tab):
    """ 
    Description: Click the visit button page
    Input: 
        main_tab: <current tab instance>
    Output:
        get the reply from the browser
    """
    # WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"🖥 Visit sites")]'))).click()
    input = main_tab.find_element(By.XPATH, '//div[@id="editable-message-text"]')
    input.click()
    wait(2)
    # Click the button to visit sites
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(Keys.DELETE)
    wait(1)
    input.send_keys("/visit")
    wait(1)
    input.send_keys(Keys.ENTER)
    # keyboard.write('visit')
    # press('enter')
    wait(2)

def ad_viewer(profile):
    """ 
    Description: View the ad with new instance of the browser
    Input: 
        profile: <Location of profile instance>
    Output:
        Keeps clicking the ads forever
    """
    # get driver to create a main_tab
    main_tab = get_driver(profile)
    print(profile)
    profile = profile.split('\\')[-2]
    print('['+profile+ '] : ' +'Getting the browser ready\n')
    main_tab.get(BASE_URL)
    # wait(main_tab) to load
    # wait for the main_tab to load
    page_loaded(main_tab)
    # set variables for future use
    print('Setting the variables and Entering the loop')
    view_time=15
    temp_link=''
    stop=1
    wait(5)
            
    while stop:
        # click the visit site to get the link
        click_visit_site(main_tab)
        wait(5)
        status_of_ads = ads_status(main_tab)
        if status_of_ads=='nomoreads':
            stop = 0
            main_tab.quit()
            wait(1)

        else:
            # links status from the url
            money_link=get_money_link(main_tab)
            view_time = open_link_in_chrome(money_link,temp_link,main_tab)
            logger('Visited Website',money_link,view_time,profile)
            view_time = 15
            temp_link=money_link
    main_tab.quit()


def runner():
    # check if new ads are avialable
    current_crypto_index=0
    while True:
        try:
            # this is done so that it doesn't pass over the given profiles
            if current_crypto_index >= len(profiles):
                current_crypto_index=0
            # this is done so that you can add profiles folder in real time
            profile = profiles[current_crypto_index]
            print('Current Profiles: '+ profile)
            ad_viewer(profile)
            current_crypto_index = current_crypto_index+1
        # this code skips the faulty profile
        except Exception as E:
            print(E)
            current_crypto_index = current_crypto_index+1
            logger(str(E),'Restarting','10',profile)
            wait(10)
            os.system("taskkill /f /im  Firefox.exe >nul 2>&1")
            #clear_cache()
            
if __name__ == "__main__":
    runner()