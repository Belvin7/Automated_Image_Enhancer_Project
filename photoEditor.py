from PIL import Image, ImageEnhance, ImageFilter
import os 

im = Image.open("instagram-pic.jpeg")

print(im.format, im.size, im.mode)