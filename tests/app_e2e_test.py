import unittest
from scandl2 import *
from scandl2_extensions import *


class app_e2e_test(unittest.TestCase):

    def test_execute(self):
        arg = "http://w14.mangafreak.net/Manga/Knights_Of_Sidonia"
        res = app.execute(arg)


if __name__ == '__main__':
    unittest.main()
