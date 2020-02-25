import os
import argparse
from importlib import import_module as imp
from util import image

def test(lang = 'ug', count = 5, out_dir = 'data/'):
    str_util = imp('lang.' + lang + '.str')

    print('Testing, images not be saved.')
    for i in range(count):
        # img = image.gen()
        img, word = str_util.genRandTextImg()
        fp = os.path.join(out_dir, 'images/word_{}.jpg'.format(i + 1))
        print('{}\t'.format(i), fp + '\t' + word)
        img.show()

if __name__ == '__main__':
    test()
