from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# BROWSER

TIME_TO_WAIT = 60 # seconds

def browser_init():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(TIME_TO_WAIT) 
    return driver

def browser_quit(browser):
    browser.quit()

# DOWNLOAD


