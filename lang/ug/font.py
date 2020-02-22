import os
import random

font_list = []

def get_rand_font():
    global font_list
    if len(font_list) == 0:
        font_name_list = os.listdir('lang/ug/fonts/')
        for font_name in font_name_list:
            font_list += ['./lang/ug/fonts/' + font_name]

    return random.choice(font_list)
