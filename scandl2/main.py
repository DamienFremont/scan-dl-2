import getopt
import glob
import json
import os
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from os.path import exists
from subprocess import call
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# STATIC **********************************************************************


# PUBLIC **********************************************************************

class Item:
    index = 0

# PRIVATE *********************************************************************

def browser_init():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(60) # seconds
    return driver

def browser_quit(browser):
    browser.quit()

def process():
    print("Start")
    items = []
    print('End')

# FUNCTIONS *********************************************************************

# LOGS *********************************************************************

# UTILS *********************************************************************

# SCRIPT **********************************************************************

def main(argv):
    process()

if __name__ == "__main__":
    main(sys.argv[1:])
