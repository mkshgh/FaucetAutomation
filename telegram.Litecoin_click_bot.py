"""
Auto telegram LTC mining BOT
"""
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
import webbrowser
from datetime import datetime
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from glob import glob
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pyperclip
pyautogui.FAILSAFE = False
""" Not used now """
# imports
# from re import A
# from fake_useragent import UserAgent
# from browser_history.browsers import Brave
# from urllib.parse import unquote
# from typing import Any
# import requests
# import keyboard
# from pywinauto import Application
# from subprocess import Popen
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as 


# functions
# from keyboard import press
# press('enter')
# to remove the popup if exists
# def clear_cache():
#     p = Popen("freeTemp.bat", cwd=r"C:\\pyteleclick\\")


# def bot_delete_the_channel(main_tab,channel_tag):
#     try:
#         # channel_to_delete
#         bot_channel_to_delete ="//div[@class= 'scroll-container']//h3[text() ='{}'']/../../../..".format(channel_tag)
#         delete_channel_button = "//div[@class='MenuItem destructive']"
#         confirm_delete_button = "//button[@class='Button confirm-dialog-button default danger text'][1]"
#         # right click button
#         actionChains = ActionChains(main_tab)
#         actionChains.move_to_element(bot_channel_to_delete).perform()
#         actionChains.context_click().perform()
#         # delete button
#         click_when_loaded(delete_channel_button)
#         # confirm delete button
#         click_when_loaded(confirm_delete_button)
#         # go to LTC bot channel
#         return 1
#     except:
#         return 0


# def get_final_url_from_browser_history(transit_url,wait_time=12):
#     """ 
#     Description: get the url of the given messsage bot given xtab is installed and only one tab is opened at a time
#     Input: 
#         transit_url: Url which will redirect to the new url
#         wait_time: Time in seconds to wait for the redirect
#     Output:
#         Final url from your desired browser, I use brave by default 
#     """ 
#     test_url = 'www.mghimire.com.np'
#     # 
#     webbrowser.get().open(transit_url)
#     wait(wait_time)
#     webbrowser.get().open_new_tab(test_url)
#     wait(2)
#     close_browser_by_name()
#     wait(1)
#     bot_url = Brave().fetch_history().histories[-1][-1]
#     # 
#     # if transit_url or test_url in bot_url:
#     #     get_final_url_from_browser_history(transit_url,wait_time=wait_time+5)
#     # else:
#     return bot_url

# variables
# bot_channel_setting_btn = "//div[@class='header-tools']//child::button[@class='Button smaller translucent round has-ripple']"
# bot_channel_select_message_btn = "//div[@class='bubble menu-container custom-scroll top right opacity-transition fast open shown']//child::i[@class='icon-select']/.."
# ltc_join_channel_button_last_seen ='(//button[starts-with(text(),"🔎 Go to channel")])[last()]'
# cache_LTC_Channel_Link_div_primary = '//div[@class="PickerSelectedItem"][1]'
# ltc_join_channel_button_last_seen ='(//button[starts-with(text(),"🔎 Go to channel")])[last()]'
# ltc_join_group_button_last_seen ='(//button[starts-with(text(),"🔎 Go to group")])[last()]'
# ltc_join_channel_button = "//div[@class='message-date-group']/div[last()]//child::button[contains(text(),'Go to channel')]"
# ltc_join_group_button = "//div[@class='message-date-group']/div[last()]//child::button[contains(text(),'Go to group')]"

ltc_all_channels='//div[@class="ripple-container"]//ancestor::div[@class="ListItem-button"]'
telegram_last_message_area = "(//div[@class='message-date-group'][last()]/div)[last()]"
ltc_channel_button = '//div[@class= "scroll-container"]//h3[text() ="LTC Click Bot"]/../../../..'
ltc_channel_command_input_field = '//div[@id="editable-message-text"]'
ltc_visit_website_button = '(//button[starts-with(text(),"🔎 Go to website")])[last()]'

ltc_last_popup_link = '(//div[@class="modal-content custom-scroll"])[last()]/a'
ltc_skip_button = '(//button[text()="⏩ Skip"])[last()]'
ltc_message_bot_button = "//div[@class='message-date-group']/div[last()]//child::button[contains(text(),'Message bot')]"
ltc_message_bot_button_last_seen ='(//button[starts-with(text(),"✉️ Message bot")])[last()]'

ltc_channel_joined_button = '(//button[starts-with(text(),"✅ Joined")])[last()]'
ltc_last_join_channel_group_button = "//div[@class='message-date-group']/div[last()]//child::button[contains(text(),'Go to ')]"

bot_channel_start_btn = "//button[@class='Button tiny primary fluid has-ripple']"
bot_channel_name = "//div[@class='chat-info-wrapper']//child::h3"

# To do :
# - Join the channels bots
# channels = 'Litecoin_click_bot'

# Global Variables
CURRENT_DIR = os.getcwd()
BASE_URL = "https://web.telegram.org/z/"
# put all the profile in the profiles folder
PROFILE_DIR = 'profiles'
LINK_START = "tg://unsafe_url?url="
IMP_DELAY = 10
profiles = glob(PROFILE_DIR+'/*/')
LTC_CHANNEL_ID='Litecoin_click_bot'


# Initialize the driver object
def get_driver(profile,zoom_level=0.8):
    """ 
    Description: New Instance of the webbrowser with given profile
    Input: 
        profile: <current profile instance>
    Output:
        Instance of the new browser
    """  
    options = FirefoxOptions()
    #options.add_argument("--headless")
    fp = webdriver.FirefoxProfile(profile)
    # zoomed out because sometimes skip button was out of view 
    fp.set_preference("layout.css.devPixelsPerPx", zoom_level)
    teleminebot = webdriver.Firefox(firefox_profile=fp,options=options)
    teleminebot.maximize_window()
    return teleminebot

def wait(delay=IMP_DELAY):
    """ Implicitly wait """
    time.sleep(delay)

def click_this_element(main_tab,element_to_click):
    """ 
    Description: Skip the faulty ad
    Input: 
        main_tab: <current tab instance>

    Output:
        Click the last given element
    """ 
    main_tab.find_element(By.XPATH,element_to_click).click()

    
def get_final_url_from_clipboard(transit_url,wait_time=10):
    """ 
    Description: get the url of the given messsage bot given xtab is installed and only one tab is opened at a time
    Input: 
        transit_url: Url which will redirect to the new url
        wait_time: Time in seconds to wait for the redirect
    Output:
        Final url from your desired browser, I use brave by default 
    """ 
    test_url = 'www.mghimire.com.np'
    # 
    pyautogui.doubleClick(x=218, y=1061)
    wait(2)
    webbrowser.get().open(transit_url)
    wait(wait_time)
    pyautogui.hotkey('alt','d')
    wait(1)
    pyautogui.hotkey('ctrl', 'c')
    bot_url = pyperclip.paste()
    wait(1)

    if transit_url.split('//')[-1] == bot_url:
        wait(2)
        pyautogui.hotkey('alt','d')
        wait(1)
        pyautogui.hotkey('ctrl', 'c')
        bot_url = pyperclip.paste()

    close_browser_by_name()

    return bot_url.split('//')[-1]

def is_time_in_range(start_time:int,end_time:int,current_time=int(datetime.now().strftime("%H"))):
    """ 
    Description: check if the given hour is between the given range of hour
    Input: 
        curret_time: time in hour 1-23 integer
                    - it is the current hour by default
        start_time: lower time limit 1-23 integer
        end_time: upper time limit  1-23 integer
    Output:
        Click the last given element
    """ 
    if start_time<current_time<end_time:
        return 1
    else:
        return 0

def click_when_loaded(main_tab,element_to_click,refresh_time=2,ttr=20,max_retries=1,refresh=False):
    """ 
    Description: click the given element when loaded
    Input: 
        main_tab: <current tab instance>
        element_to_click: Element to monitor until loaded
        element_ttl: Time interval to refresh the page if element not found in seconds
        max_retries: No. of time to perform check
        refresh_time: Check inteval in no. of seconds
        refresh: True if refresh after not success click else False by default
    Output:
        element_loaded: the element is loaded
        element_not_loaded: the element is laoded
    """
    not_loaded = 1
    view_time=0
    while not_loaded:
        if max_retries<=0:
            not_loaded=0
            return "element_not_loaded"
        if view_time>ttr:
            view_time=0
            if refresh:
                main_tab.refresh()
                ActionChains(main_tab).send_keys(Keys.ESCAPE).perform()
                max_retries = max_retries-1
                wait(2)
            else:
                return 'element_not_loaded'
        try:
            main_tab.find_element(By.XPATH,element_to_click).click()
            not_loaded=0
            return "element_loaded"
        except:
            print('Waiting 2 seconds more until {} loads'.format(element_to_click))
            wait(refresh_time)
        view_time=view_time+refresh_time

def get_text_of_element(main_tab, element):
    """ 
    Description: Get the text from the given element
    Input: 
        main_tab: <current tab instance>
        element_to_click: Element to get text from
    Output:
        text of the element
    """
    return main_tab.find_element(By.XPATH,element).text

def close_browser_by_name(browserName='Brave.exe'):
    """ 
    Description: Get the text from the given element
    Input: 
        None
    Output:
        Force closes the browser if opened
    """
    try:
        os.system("taskkill /f /im  {} >nul 2>&1".format(browserName))
    except:
        pass

def get_href_from_popup(main_tab,popup_button,link_element):
    """ 
    Description: Get the link to browser
    Input: 
        main_tab: <current tab instance>
        popup_button: button which revelas the link element
        link_element: link to the element where href link is
    Output:
        link to browse
    """
    # Keep clicking the button forever and make money
    click_this_element(main_tab,popup_button)
    wait(2)
    money_link:str = main_tab.find_element(By.XPATH,link_element).get_attribute("href")
    ActionChains(main_tab).send_keys(Keys.ESCAPE).perform()
    wait(1)
    return money_link

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
    current_time = datetime.now()
    logs_time = "{}_{}_{}_{}".format(str(current_time.year),str(current_time.month),str(current_time.day),text)
    logs_file = os.path.join('logs',(logs_time+"_logs.txt")) 
    with open(logs_file, "a+",encoding="utf-8") as f:
        logs_write='['+profile+'] , ' + str(datetime.now())+ " , " + str(text) + ', '+ str(money_link) + " , "+str(view_time)+'s\n'
        f.write(logs_write)
    print(logs_write)


def ads_status(main_tab,last_message_area):
    """ 
    Description: Status of the ad after clicking the Visit Page button
    Input:
        main_tab: <current tab instance>
        last_message_area: the area where you want to check the status
    Output:
        the status of the ad: 'NoMoreAds','VisitedSite','messagebotnow','JoinGroup',etc
    """
    last_message = main_tab.find_element(By.XPATH,last_message_area).get_attribute('innerHTML')
    not_loaded = 1
    while not_loaded:
        try:
            if ('Sorry, there are no new ads available.' in last_message):
                return "NoMoreAds"
            if ('Go to website' in last_message):
                return "VisitedSite"
            if ('You must forward a message to me from' in last_message):
                return "RetryMessageBot"
            if ('Message bot' in last_message):
                return "MessageBot"
            if ('Go to channel' in last_message):
                return "JoinChannel"
            if ('Go to group' in last_message):
                return "JoinGroup"
            if ('Visit sites' in last_message):
                print('wait 5s until the ads load')
                wait(5)
                last_message = main_tab.find_element(By.XPATH,last_message_area).get_attribute('innerHTML')
            else:
                return 'NoMoreAds'
        except:
            return 'NoMoreAds'


def send_command(main_tab,command_area,text_command):
    """ 
    Description: Click the visit button page
    Input: 
        main_tab: <current tab instance>
        command_area: area to enter the command
        text_command: what command to type in the command_area
    Output:
        removes any previous command and types/sends the command
    """
    click_when_loaded(main_tab,command_area)
    input = main_tab.find_element(By.XPATH,command_area)
    # Click the button to visit sites
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(Keys.DELETE)
    input.send_keys(text_command)
    wait(1)
    input.send_keys(Keys.ENTER)

def open_link_until_make_money(money_link,main_tab):
    """ 
    Description: open the link in the new browser, since opening in the selenium causes it to track as a bot
    Input: 
        money_link: current money link
        main_tab<current tab instance>
    Output:
        link is openeed in the default browser of your manchine.
        I use the Brave so, Brave.exe is opened here.
    """  
    wait(5)
    view_time = 5
    while True:
        last_message = main_tab.find_element(By.XPATH,telegram_last_message_area).get_attribute('innerHTML')
        if ('Sorry, there are no new ads available.' in last_message):
            return  "NoMoreAds"
        elif view_time>120:
            # skip the link
            send_command(main_tab,ltc_channel_command_input_field,'/visit')
            wait(2)
            click_this_element(main_tab,ltc_skip_button)
            return "SkipAds"
        elif money_link == get_href_from_popup(main_tab,ltc_visit_website_button,ltc_last_popup_link):
            print('adding 5s to the loop: '+str(view_time))
            wait(5)
            view_time = view_time+5
            last_message = main_tab.find_element(By.XPATH,telegram_last_message_area).get_attribute('innerHTML')
        else:
            return "VisitedSite"
            

def click_loc_xy(main_tab, x, y, left_click=True):
    """
    Input:
        dr:browser
        x:page x coordinate
        y:page y coordinate
        left_click:true is the left mouse click.
        Otherwise right click
    Output:
        Clicks right or left at the given position
    """
    if left_click:
        ActionChains(main_tab).move_by_offset(x, y).click().perform()
    else:
        ActionChains(main_tab).move_by_offset(x, y).context_click().perform()
    ActionChains(main_tab).move_by_offset(-x, -y).perform() #Restore the mouse position to before moving


def bot_delete_all_channel(main_tab,leave_top=5):
    """ 
    Description: Skip the faulty ad
    Input: 
        main_tab: <current tab instance>
        leave_top: how many channels to spare at the top
    Output:
        Click the last given element
    """ 
    all_channel_links = main_tab.find_elements_by_class_name('ListItem-button')
    total_channels = len(all_channel_links)
    while total_channels>leave_top:
        i=0
        for i in range(total_channels):
            try:
                i=i+1
                if i<leave_top:
                    print('Skipping Chanel: ',i)
                else:
                    # channel_to_delete
                    delete_channel_button = "//div[@class='MenuItem destructive']"
                    confirm_delete_button = "//button[@class='Button confirm-dialog-button default danger text'][1]"
                    # right click button
                    actionChains = ActionChains(main_tab)
                    actionChains.move_to_element(all_channel_links[i]).perform()
                    actionChains.context_click().perform()
                    # delete button
                    click_when_loaded(main_tab,delete_channel_button,ttr=4)
                    # confirm delete button
                    click_when_loaded(main_tab,confirm_delete_button,ttr=4)
                    print('deleted channel: ', i)
            except:
                i=i-1
                pass
        # Refresh the page and check for the 
        main_tab.refresh()
        wait(2)
        ActionChains(main_tab).send_keys(Keys.ESCAPE).perform()
        wait(2)
        all_channel_links = main_tab.find_elements_by_class_name('ListItem-button')
        total_channels = len(all_channel_links)
    


def forward_this_message(main_tab,channel='new'):
    """ 
    Description: get the url of the given messsage bot
    Input: 
        channel: 
        -   'new' if forward from a new message group default
        -   'self' if forward to same channel
        -   'subscribe' if subscribing to new channel

        main_tab <current tab instance>
    Output:
        Message forwarded to where you want
    """ 
    #Forward the message variables
    bot_channel_name = "//div[@class='chat-info-wrapper']//child::h3"
    bot_channel_start_btn = "//button[@class='Button tiny primary fluid has-ripple']"
    ltc_last_message = "//div[@class='message-date-group']/div[last()]"
    bot_forward_button = "//div[@class='MessageSelectToolbar-inner']//child::i[@class='icon-forward']/.."
    bot_ltc_channel_button = "//div[@class='modal-dialog']//child::h3[text()='LTC Click Bot']//ancestor::div[@class='ListItem-button']"
    bot_ltc_send_button = "//button[@class='Button send  default secondary round']"
    ltc_last_message_link = "(//div[@class='message-date-group'][last()]/div)[last()]//a"
    ltc_setting_btn= "//div[@class='HeaderActions']//i[@class='icon-more']/.."
    ltc_select_btn= "//div[@class='bubble menu-container custom-scroll top right opacity-transition fast open shown']//i[@class='icon-select']/.."
    window_x = main_tab.get_window_size()['width']/2
    window_y = main_tab.get_window_size()['height']
    
    if channel=='self':
        bot_channel="LTC_CLICK_BOT"
        
    elif channel=='new':
        click_when_loaded(main_tab,ltc_last_message_link)
        click_when_loaded(main_tab,bot_channel_start_btn,ttr=6)
        # name of the channel
        bot_channel = get_text_of_element(main_tab,bot_channel_name)
    # if channel is subscribe
    else:
        click_when_loaded(main_tab,bot_channel_start_btn,ttr=6)
        bot_channel=get_text_of_element(main_tab,bot_channel_name)
    
    click_when_loaded(main_tab,ltc_setting_btn)
    click_when_loaded(main_tab,ltc_select_btn)
    # if unable to find the last element after selecting the item, and it keeps happening somehow
    if click_when_loaded(main_tab,ltc_last_message,ttr=4)=='element_not_loaded':
        # click on the center of the webapge and hope it clicks something
        click_loc_xy(main_tab,window_x,int(0.5*window_y))
    click_when_loaded(main_tab,bot_forward_button)
    click_when_loaded(main_tab,bot_ltc_channel_button)
    click_when_loaded(main_tab,bot_ltc_send_button)
    return bot_channel



def visit_link_for_time(intial_url,wait_time=11):
    """ 
    Description: get the url of the given messsage bot
    Input: 
        intial_url: Url which will redirect to the new url
        wait_time: Time in seconds to wait for the redirect
    Output:
        Final url from your desired browser, I use brave by default 
    """ 
    webbrowser.open(intial_url)
    wait(wait_time)
    close_browser_by_name()

        

def message_bot(main_tab,profile):
    """ 
    Description: Message the bot until finished
    Input: 
        main_tab <current tab instance>
        profile: current profile directory
    Output:
        Message Bot until finished
    """ 
        # Start messaging the Bots Second
    send_command(main_tab,ltc_channel_command_input_field,'/bots')
    visit_message_bot_stop=1
    wait(5)
    while visit_message_bot_stop:
        #  the visit site to get the link
        tic = time.perf_counter()
        status_of_ads = ads_status(main_tab,telegram_last_message_area)
        
        if status_of_ads=='NoMoreAds':
            logger('NoMoreAds','Restarting','10',profile)
            visit_message_bot_stop = 0
            return 1
        
        elif status_of_ads=='MessageBot':
            # links status from the visit website button
            bot_link=get_href_from_popup(main_tab,ltc_message_bot_button,ltc_last_popup_link)
            wait(2)
            # visit website for compliance of the offer
            visit_link_for_time(bot_link)
            # forward to oneself to reveal the channel link
            forward_this_message(main_tab,channel='self')
            wait(2)
            # forward the actuall needed channeld link
            bot_channel_name = forward_this_message(main_tab,channel='new')
            wait(2)
            # open bots command again
            send_command(main_tab,ltc_channel_command_input_field,'/bots')
            wait(2)
            # check if the last message has message button in it
            try:
                if bot_link == get_href_from_popup(main_tab,ltc_message_bot_button,ltc_last_popup_link):
                    wait(2) 
                    click_when_loaded(main_tab,ltc_skip_button)
                    wait(2)
                    toc = time.perf_counter()
                    logger("SkippedAds",bot_channel_name,round(toc-tic,2),profile)
                    wait(2)
                else:
                    toc = time.perf_counter()
                    logger('MessageBot',bot_channel_name,round(toc-tic,2),profile)
            except:
                toc = time.perf_counter()
                logger('MessageBot',bot_channel_name,round(toc-tic,2),profile)
                    

def visit_website(main_tab,profile):
    # Start Vsiting the website first
    """ 
    Description: Visit website until finished
    Input: 
        main_tab <current tab instance>
        profile: current profile directory
    Output:
        Visit website until finished
    """ 
    send_command(main_tab,ltc_channel_command_input_field,'/visit')
    visit_website_stop=1
    wait(5)
    while visit_website_stop:
        tic = time.perf_counter()         
        #  the visit site to get the link
        status_of_ads = ads_status(main_tab,telegram_last_message_area) 
        if status_of_ads=='NoMoreAds':
            toc = time.perf_counter()
            logger('NoMoreAds','Restarting',round(toc-tic,2),profile)
            visit_website_stop = 0
            return 1
        
        else:
            # links status from the visit website button
            money_link=get_href_from_popup(main_tab,ltc_visit_website_button,ltc_last_popup_link)
            wait(2)
            webbrowser.open(money_link)
            adsStatus = open_link_until_make_money(money_link,main_tab)
            close_browser_by_name()
            toc = time.perf_counter()
            logger(adsStatus,money_link,round(toc-tic,2),profile)
            print('Closing Browser')


# .....................
    
def search_and_goto_channel_by_name(main_tab,channel_name):
    """ 
    Description: Search channel by and go to it
    Input: 
        channel_name: Name of telegram_channel_name you want to join
        main_tab: <Location of main_tab instance>
    Output:
        Keeps clicking the ads forever
    """
    bot_search_box = "//input[@id='telegram-search-input']" 
    search_bot_channel_div = "//child::span[contains(text(),'{}')]//ancestor::div[@class='ListItem-button']".format(channel_name)
    alternative_bot_channel_div = '//div[@class="ListItem chat-item-clickable search-result no-selection"][1]'
    cache_LTC_Channel_Link_div = '//div[@class="search-section"][1]//div[@class="ListItem chat-item-clickable search-result no-selection"][1]'
    send_command(main_tab,bot_search_box,channel_name)
    wait(1)
    if channel_name=="Litecoin_click_bot":
        click_when_loaded(main_tab,cache_LTC_Channel_Link_div)
            
    elif click_when_loaded(main_tab,search_bot_channel_div,ttr=4)=='element_not_loaded':
        click_when_loaded(main_tab,alternative_bot_channel_div)
       


def join_this_channel_and_return_back(main_tab,channel_tag,original_channel='Litecoin_click_bot'):
    """ 
    Description: Join channel by name and return back to the original channel
    Input: 
        channel_name: Name of telegram_channel_name you want to join
        main_tab: <Location of main_tab instance>
    Output:
        Keeps clicking the ads forever
    """
    channel_tag = 't.me/'+channel_tag
    channel_link = '(//a[starts-with(text(),"{}")])[last()]'.format(channel_tag)
    # send and click the channel link
    send_command(main_tab,ltc_channel_command_input_field,channel_tag)
    click_when_loaded(main_tab,channel_link,ttr=6)
    # Click subscribe / Join Button
    click_when_loaded(main_tab,bot_channel_start_btn,ttr=6)
    # return to 
    if click_when_loaded(main_tab,ltc_channel_button,ttr=6)== 'element_not_found':
        search_and_goto_channel_by_name(main_tab,original_channel)
    click_when_loaded(main_tab,ltc_channel_joined_button)
    wait(2)

def join_channel(main_tab,profile,run_times=13):
    """ 
    Description: Join a channel to make money
    Input: 
        profile: <Location of profile instance>
        main_tab: <Location of main_tab instance>
    Output:
        Keeps joinging the paid channel forever
    """
        # Start Joining the Channel third
    send_command(main_tab,ltc_channel_command_input_field,'/join')
    join_channel_start=1
    wait(5)
    while join_channel_start:
        print('{} times running'.format(run_times))
        if run_times < 0:
            raise Exception('Stopping at {} times'.format(run_times+21))
            join_channel_start = 0
        #  the visit site to get the link
        tic = time.perf_counter()
        status_of_ads = ads_status(main_tab,telegram_last_message_area)
        
        if status_of_ads=='NoMoreAds':
            logger('NoMoreAds','Restarting','10',profile)
            join_channel_start = 0
            return 1
        
        elif status_of_ads=='JoinChannel' or status_of_ads=='JoinGroup':
            # links status from the visit website button
            bot_link=get_href_from_popup(main_tab,ltc_last_join_channel_group_button,ltc_last_popup_link)
            # Get the channel name from the browser history
            channel_link = get_final_url_from_clipboard(bot_link)
            channel_tag = channel_link.split('/')[-1].split('?')[0]
            # Search and traverse to the channel
            join_this_channel_and_return_back(main_tab,channel_tag)
            # open bots command again
            send_command(main_tab,ltc_channel_command_input_field,'/join')
            wait(3)
            
            # check if the last message has Join Channel Button in it
            try:
                if bot_link == get_href_from_popup(main_tab,ltc_last_join_channel_group_button,ltc_last_popup_link):
                    wait(2) 
                    click_when_loaded(main_tab,ltc_skip_button)
                    wait(2)
                    toc = time.perf_counter()
                    logger("SkippedAds",channel_tag,round(toc-tic,2),profile)
                    wait(2)
                else:
                    toc = time.perf_counter()
                    logger('JoinChannel',channel_tag,round(toc-tic,2),profile)
                    run_times=run_times-1
            except Exception as E:
                run_times=run_times-1
                toc = time.perf_counter()
                logger('JoinChannel',channel_tag,round(toc-tic,2),profile)


def ppc_viewer(profile):
    """ 
    Description: Pay per click for LTC BOT
    Input: 
        profile: <Location of profile instance>
        main_tab: <Location of main_tab instance>
    Output:
        Keeps clicking the ads forever
    """
    # check today
    # start the browser and go to the main page
    print(profile)
    main_tab = get_driver(profile)
    profile = profile.split('\\')[-2]
    print('['+profile+'] : ' +'Getting the browser ready\n')
    main_tab.get(BASE_URL)
    # get driver to create a main_tab
    # wait(main_tab) to load
    # wait for the main_tab to load
    click_when_loaded(main_tab,ltc_channel_button,ttr=20,max_retries=4,refresh=True)
    # set variables for future use
    print('Setting the variables and Entering the loop')
    wait(5)
    try:
        message_bot(main_tab,profile)
    except Exception as E:
        logger('error',str(E),'10',profile)
        close_browser_by_name()
        print(str(E))
    
    try:
        visit_website(main_tab,profile)
    except:
        print(str(E))
        logger('error',str(E),'10',profile)
        close_browser_by_name()
    
    try:
        join_channel(main_tab,profile,run_times=5)
    except Exception as E:
        print(str(E))
        logger('error',str(E),'10',profile)
        close_browser_by_name()
    
    # delete channels between the given time interval only
    # if is_time_in_range(14,16):
    # bot_delete_all_channel(main_tab)
    main_tab.quit()


def runner():
    # check if new ads are avialable
    current_crypto_index=4
    while True:
        try:
            # this is done so that it doesn't pass over the given profiles
            if current_crypto_index >= len(profiles):
                current_crypto_index=0
            # this is done so that you can add profiles folder in real time
            profile = profiles[current_crypto_index]
            print('Current Profiles: '+ profile)
            # Start viewing the ads now
            ppc_viewer(profile)
            current_crypto_index = current_crypto_index+1
        # this code skips the faulty profile
        except Exception as E:
            print(str(E))
            current_crypto_index = current_crypto_index+1
            logger('error',str(E),'10',profile)
            wait(10)
            close_browser_by_name(browserName='Firefox.exe')
            #clear_cache()

if __name__ == "__main__":
    runner()
