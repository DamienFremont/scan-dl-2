import unittest
from scandl2 import *
from scandl2 import plugin


class app_test(unittest.TestCase):

    def test_get_plugin_mangafreak(self):
        res = plugin.get_plugin('mangafreak')
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()
