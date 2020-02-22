from PIL import Image
from util.color import getRandHex

def gen():
    img = Image.new(mode = "RGB",
                    size = (200, 100),
                    color = getRandHex())
    return img
