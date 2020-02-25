from PIL import Image
from util.color import getRandHex

def gen(size):
    img = Image.new(mode = "RGB",
                    size = size,
                    color = getRandHex())
    return img
