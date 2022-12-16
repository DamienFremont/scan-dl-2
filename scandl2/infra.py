from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
from fpdf import FPDF, HTMLMixin
import re
import urllib
from urllib.parse import urlparse

# BROWSER

TIME_TO_WAIT = 60  # seconds


def browser_init():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(TIME_TO_WAIT)
    return driver


def browser_quit(browser):
    browser.quit()

# FILES


DATE_FMT = "%Y%m%d_%H%M%S"


def files_create_ouput():
    now = datetime.datetime.now()
    target_dir = os.path.join('.output', f"{now.strftime(DATE_FMT)}")
    os.makedirs(target_dir)
    return target_dir

# DOWNLOAD


def web_download(url, dir, i, referer):
    out = os.path.join(dir, f"img-{i:06d}.jpg")
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Referer': referer})
    res = urllib.request.urlopen(req)
    fo = open(out, 'wb')
    fo.write(res.read())
    fo.close()
    return out

# PDF


FORMAT = 'A5'


def pdf_create(files, dest, filename):
    out = os.path.join(dest, f"{filename}.pdf")

    class PDF(FPDF, HTMLMixin):
        pass
    pdf = PDF(format=FORMAT)
    for i in range(0, len(files)):
        file = files[i]
        pdf.add_page()
        pdf.image(file, x=0, y=0, w=pdf.w, h=pdf.h)
    pdf.output(out, 'F')
    return out


def slugify(value, allow_unicode=False):
    return re.sub(r'\W+', '', value)

# WEB


def get_site(url):
    netloc = urlparse(url).netloc
    parts = netloc.split('.')
    if(len(parts) == 2):
        return netloc.split('.')[0]
    return netloc.split('.')[1]
