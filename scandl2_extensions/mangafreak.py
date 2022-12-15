from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class mangafreak():

    def get_serie_title(browser, url):
        browser.get(url)
        return browser.find_element(By.CSS_SELECTOR, '.manga_series_info h5').text

    def get_chapter_url_list(browser, url):
        browser.get(url)
        arr1 = browser.find_elements(By.CSS_SELECTOR, '.manga_series_list tr a:not([download])')
        arr2 = [None] * len(arr1)
        for i in range(0, len(arr2)):
            arr2[i] = arr1[i].get_attribute('href')
        return arr2

    def get_page_url_list(browser, url):
        browser.get(url)
        arr1 = browser.find_elements(By.CSS_SELECTOR, '.read_selector option')
        arr2 = [None] * len(arr1)
        for i in range(0, len(arr2)):
            arr2[i] = browser.find_element(By.CSS_SELECTOR, f".slideshow-container .mySlides:nth-child({i+1}) img").get_attribute('src')
        return arr2

    def get_page_img_url(browser, url):
        return url
