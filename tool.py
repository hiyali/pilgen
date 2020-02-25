import os
from importlib import import_module as imp

def util(lang = 'ug', out_dir = 'data/'):
    str_util = imp('lang.' + lang + '.str')

    print('Preparing char_list of `{}`:'.format(lang))
    char_list = str_util.getCharList()
    # print(char_list)

    os.makedirs(out_dir, exist_ok=True)
    fp = os.path.join(out_dir, 'char_list.txt')

    clf = open(fp, "w")
    clf.write(''.join(char_list))

    print('The char_list[{}] written into `{}`'.format(len(char_list), fp))

if __name__ == '__main__':
    util()
