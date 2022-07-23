from Help_Fn.functions import *

class Test():
    def __init__(self):
        self.meta_data = Meta_data()
        print(self.meta_data.read('f:\Work area\KKI\Global_collection\DataFaces\Melania Tramp\\31300.jpg'))
        print(self.meta_data.read('f:\Work area\KKI\Global_collection\DataFaces\Melania Tramp\\43950.jpg'))

test = Test()