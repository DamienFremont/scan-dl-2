import imp
import unittest
import scandl2

class mangafreak_plugin_test(unittest.TestCase):

    def setUp(self):
        self.browser = scandl2.browser_init()

    def tearDown(self):
        self.browser.quit()

    def test_get_serie_title(self):
        arg = "http://w14.mangafreak.net/Manga/Knights_Of_Sidonia"
        res = scandl2.mangafreak_plugin.get_serie_title(self.browser, arg)
        self.assertEqual('KNIGHTS OF SIDONIA', res)

    def test_get_page_img_url(self):
        arg = "http://w14.mangafreak.net/Read1_Knights_Of_Sidonia_1"
        res = scandl2.mangafreak_plugin.get_page_img_url(self.browser, arg)
        self.assertEqual('https://images.mangafreak.net/mangas/knights_of_sidonia/knights_of_sidonia_1/knights_of_sidonia_1_1.jpg',res)


if __name__ == '__main__':
    unittest.main()
