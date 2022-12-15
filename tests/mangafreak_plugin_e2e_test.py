import unittest
from scandl2 import *
from scandl2_extensions import *

class mangafreak_plugin_e2e_test(unittest.TestCase):

    def setUp(self):
        self.browser = infra.browser_init()

    def tearDown(self):
        self.browser.quit()

    def test_get_serie_title(self):
        arg = "http://w14.mangafreak.net/Manga/Knights_Of_Sidonia"
        res = mangafreak_plugin.get_serie_title(self.browser, arg)
        self.assertEqual('KNIGHTS OF SIDONIA', res)

    def test_get_chapter_url_list(self):
        arg = "http://w14.mangafreak.net/Manga/Knights_Of_Sidonia"
        res = mangafreak_plugin.get_chapter_url_list(self.browser, arg)
        self.assertTrue(len(res) > 0)
        self.assertTrue('http://w14.mangafreak.net/Read1_Knights_Of_Sidonia_1', res[0])
        self.assertTrue('http://w14.mangafreak.net/Read1_Knights_Of_Sidonia_2', res[1])

    def test_get_page_url_list(self):
        arg = "http://w14.mangafreak.net/Read1_Knights_Of_Sidonia_1"
        res = mangafreak_plugin.get_page_url_list(self.browser, arg)
        self.assertTrue(len(res) > 0)
        self.assertTrue('https://images.mangafreak.net/mangas/knights_of_sidonia/knights_of_sidonia_1/knights_of_sidonia_1_1.jpg', res[0])
        self.assertTrue('https://images.mangafreak.net/mangas/knights_of_sidonia/knights_of_sidonia_1/knights_of_sidonia_1_2.jpg', res[1])

    def test_get_page_img_url(self):
        arg = "http://w14.mangafreak.net/Read1_Knights_Of_Sidonia_1"
        res = mangafreak_plugin.get_page_img_url(self.browser, arg)
        self.assertEqual('https://images.mangafreak.net/mangas/knights_of_sidonia/knights_of_sidonia_1/knights_of_sidonia_1_1.jpg', res)

if __name__ == '__main__':
    unittest.main()
