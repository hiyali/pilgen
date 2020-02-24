import os
import argparse
from importlib import import_module as imp
from util import image

def gen(lang = 'ug', count = 100, out_dir = 'data/'):
    str_util = imp('lang.' + lang + '.str')

    os.makedirs(os.path.join(out_dir, 'images'), exist_ok=True)
    fp_gt = os.path.join(out_dir, "gt.txt")
    gtf = open(fp_gt, "w") # gt-file

    for i in range(count):
        img = image.gen()
        img, word = str_util.putRandText(img)
        # img.show()
        fp_rlyt = 'images/word_{}.jpg'.format(i + 1)
        fp_root = os.path.join(out_dir, fp_rlyt)
        img.save(fp_root)

        gtf.write(fp_rlyt + '\t' + word + '\n') # choose fp_rlyt or fp_root

    print('The leading content written into `{}`'.format(fp_gt))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Pilgen - Python Image & Label dataset generator')

    parser.add_argument('--lang', dest='Language', default='ug', help='Choose a language (default: ug)')
    parser.add_argument('--count', dest='Count', default=100, type=int, help='Set generate counts (default: 100)')
    parser.add_argument('--out-dir', dest='OutputDir', default='data/', help='Set output directory (default: data/)')

    args = parser.parse_args()

    gen(args.Language, args.Count, args.OutputDir)
