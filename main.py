import pytest
from selenium import webdriver
import sys
from selenium.webdriver.remote.remote_connection import LOGGER
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
LOGGER.setLevel(logging.FATAL)
#Signs in for you with params below if False. If it breaks, just sign in manually! After manual sign in, press enter in the console to continue
manual_sign_in = False
#If manual_sign_in True then ignore following
username = "EMAIL/USERNAME HERE"
password = "PASSWORD HERE"
#item full URL
itemurl = "https://www.ebay.com/itm/{itm id here}"
#your bidding price for the snipe as a string
bidprice = "1"
#recommended 5 seconds before bid end since grabbing methods aren't perfect
earlysecs = 5
def ebaySnipe():
   chrome_driver = webdriver.Chrome()
   chrome_driver.get('https://www.ebay.com/')
   if manual_sign_in == False:
       sleep(2)
       login = chrome_driver.find_element("xpath", "//a[@_sp='m570.l1524']")
       sleep(2)
       login.click()
       sleep(3)
       usernamespot = chrome_driver.find_element("xpath", "//input[@id='userid']")
       
       usernamespot.send_keys(username);
       sleep(1)
       continuebtn = chrome_driver.find_element("xpath", "//button[@id='signin-continue-btn']")
       continuebtn.click()
       sleep(3)
       passwordspot = chrome_driver.find_element("xpath", "//input[@id='pass']")
       passwordspot.send_keys(password)
       sleep(1)
       finalsignbtn = chrome_driver.find_element("xpath", "//button[@id='sgnBt']")
       finalsignbtn.click()
       sleep(3)
       

   else:
        input("Press enter when done authenticating: ")
   chrome_driver.get(itemurl)
   sleep(3)
   bidbutton = chrome_driver.find_element("xpath", "//a[@data-cta='placebid']")
   bidbutton.click()
   sleep(1)
   scarybid = chrome_driver.find_element("xpath", "//input[@id='app-bidlayer-bidsection-input']")
   scarybid.send_keys(bidprice)
   scarybidbutton = chrome_driver.find_elements("xpath", "//button[@class='button-placebid']")
   sleep(1)
   try:
    spoopybidtime = chrome_driver.find_element("xpath", "//span[@id='_counter_itemEndDate']")
    print(spoopybidtime)
    finalbidtime = spoopybidtime.get_attribute('data-secondsleft')
    print(finalbidtime)
    print("Waiting", finalbidtime, "seconds")
    #sleep(5)
    sleep(int(finalbidtime) - earlysecs)
    scarybidbutton[3].click()
    print("Bid sent in, good luck soldier")
    sleep(99999)
   except:
    print("Oops! We can't scrape exact time until the bid has less than 24 hours left! Try again when item is dropping within the next 24 hours!")
ebaySnipe()
