#!/usr/bin/python

import os
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFont, ImageDraw




W, H = (500,900)
msg = "15"
font = ImageFont.truetype("AppleGothic.ttf", 50)

im = Image.new("RGB",(W,H),"#EC1C24")
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)
#draw.text(((W-w)/2,(H-h)/2), msg, fill="black",font = font)
draw.text((w,(H-h)/2), msg, fill="black",font = font)


psize = 50
image = Image.new(mode = 'RGB', size = (psize,psize))
draw = ImageDraw.Draw(image)

# use a bitmap font
#font = ImageFont.truetype("AppleGothic.ttf", 15)

draw = ImageDraw.Draw(image)
draw.multiline_text(xy = (psize/2,psize/2), text = "15", font=font, align = 'center')

image.show()

im.show()
# use a truetype font
#font = ImageFont.truetype("arial.ttf", 15)

#draw.text((10, 25), "world", font=font)
