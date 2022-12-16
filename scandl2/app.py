
from scandl2 import infra
from scandl2_extensions import mangafreak
import time


# PUBLIC **********************************************************************


def execute(url):
    print("Start")
    browser = setUp()

    plugin = mangafreak

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
        time.sleep(3)

    print(f"STEP: imgs")
    for i in range(0, len(pages)):
        inp = pages[i]
        print(f"input item: {inp}")
        out = plugin.get_page_img_url(browser, inp)
        imgs.append(out)
        print(f"output item: {out}")
        time.sleep(3)

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
        out = infra.web_download(inp)
        files.append(out)
        print(f"output item: {out}")
        time.sleep(3)

    # PDF JOB
    print(f"JOB: pdf")
    print(f"input item: {dir}")
    filename = infra.slugify(title)
    out = infra.pdf_create(dir, files, 'filename')
    print(f"output item: {out}")

    print('End')
    tearDown(browser)


def setUp():
    return infra.browser_init()


def tearDown(browser):
    browser.quit()

# PRIVATE *********************************************************************
