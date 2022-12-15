
import time, requests, os, datetime
from scandl2 import infra
from scandl2_extensions import mangafreak

# PUBLIC **********************************************************************
  
DATE_FMT = "%Y%m%d_%H%M%S"

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
    now = datetime.datetime.now()
    target_dir = os.path.join('.output', f"{now.strftime(DATE_FMT)}")
    os.makedirs(target_dir)
    print(f"output item: {target_dir}")

    print(f"STEP: download")
    dir = os.path.join(target_dir, 'img')
    os.makedirs(dir)
    for i in range(0, len(imgs)):
        inp = imgs[i]
        print(f"input item: {inp}")
        res = requests.get(inp, allow_redirects=True)
        out = os.path.join(dir, f"img-{i:06d}.jpg")
        open(out, 'wb').write(res.content)
        print(f"output item: {out}")
        time.sleep(3)

    # PDF JOB
    

    print('End')
    tearDown(browser)


def setUp():
    return infra.browser_init()


def tearDown(browser):
    browser.quit()

# PRIVATE *********************************************************************
