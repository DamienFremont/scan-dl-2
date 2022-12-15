
from scandl2 import infra

# PUBLIC **********************************************************************

def execute(url):
    print("Start")
    browser = setUp()
    items = []
    print('End')
    tearDown(browser)

def setUp():
    return infra.browser_init()

def tearDown(browser):
    browser.quit()

# PRIVATE *********************************************************************
