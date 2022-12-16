
from scandl2 import infra
from scandl2.plugin import get_plugin
import time

# PUBLIC **********************************************************************

ITEM_SLEEP_INTERVAL = 0  # secondes


def execute(url):
    print("Start")
    browser = setUp()

    site = infra.get_site(url)
    plugin = get_plugin(site)
    print(f"plugin: {site}")

    print(f"JOB: find")

    print(f"STEP: title")
    title = plugin.get_serie_title(browser, url)
    out = title
    print(f"item: {out}")

    chapters = []
    pages = []
    imgs = []

    print(f"STEP: chapters")
    inp = url
    print(f"input item: {inp}")
    arr = plugin.get_chapter_url_list(browser, inp)
    for i in range(0, len(arr)):
        out = arr[i]
        chapters.append(out)
        print(f"output item: {out}")

    print(f"STEP: pages")
    for i in range(0, len(chapters)):
        inp = chapters[i]
        print(f"input item: {inp}")
        arr = plugin.get_page_url_list(browser, inp)
        for i in range(0, len(arr)):
            out = arr[i]
            pages.append(out)
            print(f"output item: {out}")
        time.sleep(ITEM_SLEEP_INTERVAL)

    print(f"STEP: imgs")
    for i in range(0, len(pages)):
        inp = pages[i]
        print(f"input item: {inp}")
        out = plugin.get_page_img_url(browser, inp)
        imgs.append(out)
        print(f"output item: {out}")
        time.sleep(ITEM_SLEEP_INTERVAL)

    # DOWNLOAD JOB
    print(f"JOB: download")

    print(f"RES: create target folder")
    dir = infra.files_create_ouput()
    print(f"output item: {dir}")

    print(f"STEP: download")
    files = []
    for i in range(0, len(imgs)):
        inp = imgs[i]
        print(f"input item: {inp}")
        out = infra.web_download(inp, dir, i, url)
        files.append(out)
        print(f"output item: {out}")
        time.sleep(ITEM_SLEEP_INTERVAL)

    # PDF JOB
    print(f"JOB: pdf")
    print(f"input item: {dir}")
    filename = infra.slugify(title)
    out = infra.pdf_create_from_imgs(files, dir, filename)
    print(f"output item: {out}")

    print('End')
    tearDown(browser)


def setUp():
    return infra.browser_init()


def tearDown(browser):
    browser.quit()

# PRIVATE *********************************************************************
