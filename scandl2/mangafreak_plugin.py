from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_serie_title(browser, url):
    browser.get(url)
    return browser.find_element(By.CSS_SELECTOR, '.manga_series_info h5').text

# def get_chapter_url_list(browser, url):

# def get_page_url_list(browser, url):

def get_page_img_url(browser, url):
    browser.get(url)
    return browser.find_element(By.CSS_SELECTOR, '.read_image div[style*="display: block;"] img').get_attribute('src')
