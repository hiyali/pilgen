# Author: Salam Hiyali
# Email: hiyali920@gmail.com
# 2020.2.22

import random
from PIL import ImageFont, ImageDraw
from lang.ug.font import get_rand_font
from lang.ug.util.bedit import uly_2_ug
from lang.ug.util.convert import br_2_pf, get_char_list
from util.color import getRandHex
from util import image

# 'vowel' - Sozuq Tawush
# None - Üzük Tawush
uly_char_map = {
    'ﺎﺋ': { 'Type': 'vowel', 'Latin': ['a', 'A'] },
    'ﺏ':  { 'Type':  None  , 'Latin': ['b', 'B'] },
    'ﭺ':  { 'Type':  None  , 'Latin': ['ch', 'Ch'] },
    'ﺩ':  { 'Type':  None  , 'Latin': ['d', 'D'] },
    'ﻪﺋ': { 'Type': 'vowel', 'Latin': ['e', 'E'] },
    'ﯥﺋ': { 'Type': 'vowel', 'Latin': ['é', 'É'] },
    'ﻑ':  { 'Type':  None  , 'Latin': ['f', 'F'] },
    'ﻍ':  { 'Type':  None  , 'Latin': ['g', 'G'] },
    'ﮒ':  { 'Type':  None  , 'Latin': ['gh', 'Gh'] },
    'ﮪ':  { 'Type':  None  , 'Latin': ['h', 'H'] },
    'ﻰﺋ': { 'Type': 'vowel', 'Latin': ['i', 'I'] },
    'ﺝ':  { 'Type':  None  , 'Latin': ['j', 'J'] },
    'ك':  { 'Type':  None  , 'Latin': ['k', 'K'] },
    'ل':  { 'Type':  None  , 'Latin': ['l', 'L'] },
    'م':  { 'Type':  None  , 'Latin': ['m', 'M'] },
    'ن':  { 'Type':  None  , 'Latin': ['n', 'N'] },
    'ڭ':  { 'Type':  None  , 'Latin': ['ng', 'Ng'] },
    'ﻮﺋ': { 'Type': 'vowel', 'Latin': ['o', 'O'] },
    'ﯚﺋ': { 'Type': 'vowel', 'Latin': ['ö', 'Ö'] },
    'پ':  { 'Type':  None  , 'Latin': ['p', 'P'] },
    'ق':  { 'Type':  None  , 'Latin': ['q', 'Q'] },
    'ر':  { 'Type':  None  , 'Latin': ['r', 'R'] },
    'س':  { 'Type':  None  , 'Latin': ['s', 'S'] },
    'ش':  { 'Type':  None  , 'Latin': ['sh', 'Sh'] },
    'ت':  { 'Type':  None  , 'Latin': ['t', 'T'] },
    'ﯘﺋ': { 'Type': 'vowel', 'Latin': ['u', 'U'] },
    'ﯜﺋ': { 'Type': 'vowel', 'Latin': ['ü', 'Ü'] },
    # v
    'ۋ':  { 'Type':  None  , 'Latin': ['w', 'W'] },
    'خ':  { 'Type':  None  , 'Latin': ['x', 'X'] },
    'ي':  { 'Type':  None  , 'Latin': ['y', 'Y'] },
    'ز':  { 'Type':  None  , 'Latin': ['z', 'Z'] },
    'ژ':  { 'Type':  None  , 'Latin': ['zh', 'Zh'] }
}

uly_cc = [] # uly char config list
uly_vcc = [] # uly vowel char config list
uly_nvcc = [] # uly not vowel char config list

def filterVowels(uly_cc_c):
    if uly_cc_c['Type'] == 'vowel':
        return True

def filterNotVowels(uly_cc_c):
    if uly_cc_c['Type'] == None:
        return True

# get random uly char config
def grucc(ch_type = ''):
    global uly_cc
    global uly_vcc
    global uly_nvcc

    if len(uly_cc) == 0:
        uly_cc = list(uly_char_map.values())
        uly_vcc = list(filter(filterVowels, uly_cc))
        uly_nvcc = list(filter(filterNotVowels, uly_cc))

    if ch_type == 'vowel':
        return random.choice(uly_vcc)
    elif ch_type == 'not_vowel':
        return random.choice(uly_nvcc)
    else:
        return random.choice(uly_cc)

# simple random uly word generator, could optimize
def gen_rand_uly_word():
    count = random.randint(8,16)
    prev = None # record previous char is vowel or not
    prevb = None # record previous before previous char is vowel or not
    word = ''

    for i in range(count):
        if prev == 'vowel':
            cc = grucc('not_vowel')
            prevb = prev
            prev = 'not_vowel'
            word += cc['Latin'][0]
            continue
        elif prev == 'not_vowel': # prevb ==
            cc = grucc('vowel')
            prevb = prev
            prev = 'vowel'
            word += cc['Latin'][0]
            continue

        cc = grucc()
        prevb = prev
        prev = 'vowel' if cc['Type'] == 'vowel' else 'not_vowel'
        word += cc['Latin'][1]
        continue

    return word

def get_rand_word():
    uly_str = gen_rand_uly_word()
    ug_str = uly_2_ug(uly_str)
    res = br_2_pf(ug_str)
    return res

def get_rand_font_size(word_len):
    size = random.randint(30, 60 - int(1.5 * word_len))
    return size

def genRandTextImg():
    word = get_rand_word()
    put_word = ''.join(reversed(word)) # for put into the img
    font = ImageFont.truetype(get_rand_font(), get_rand_font_size(len(put_word)))
    size = font.getsize(put_word)
    img = image.gen((size[0] + 10, size[1] + 10))
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), put_word, font = font, fill = getRandHex())
    return img, word

def getCharList():
    return get_char_list()
