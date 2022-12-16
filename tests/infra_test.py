import unittest
from scandl2 import *
from scandl2_extensions import *


class infra_test(unittest.TestCase):

    def test_pdf_create(self):
        files = [
            '.output/20221215_235755/img-000000.jpg',
            '.output/20221215_235755/img-000001.jpg',
            '.output/20221215_235755/img-000002.jpg',
            '.output/20221215_235755/img-000003.jpg'
        ]
        res = infra.pdf_create(files, '.output/20221215_235755', infra.slugify('1/3 NO KARESHI'))


if __name__ == '__main__':
    unittest.main()
