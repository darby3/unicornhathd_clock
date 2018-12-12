#!/usr/bin/env python

import colorsys
import datetime
import time
import random
from sys import exit
from PIL import Image, ImageDraw, ImageFont
import unicornhathd


# FONT = ('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 10)
FONT = ('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 9)

width, height = unicornhathd.get_shape()

unicornhathd.rotation(90)
unicornhathd.brightness(0.25)

text_x = 0 
text_y = 0
offset = 8 

font_file, font_size = FONT

SAMPLE_CHARACTER = '0'

font = ImageFont.truetype(font_file, font_size)
text_width, text_height = font.getsize(SAMPLE_CHARACTER)

text_width += width + text_x

try:
    while True:
        current_time = datetime.datetime.now().strftime('%I%M')
        current_seconds = int(datetime.datetime.now().strftime('%S')) * 3
        print (current_seconds)

        TEXT_UL = current_time[0] 
        TEXT_UR = current_time[1]
        TEXT_LL = current_time[2]
        TEXT_LR = current_time[3]

        image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))

        draw = ImageDraw.Draw(image)
        draw.text((text_x, text_y), TEXT_UL, fill=(0, 100, current_seconds), font=font)
        draw.text((text_x + offset, text_y), TEXT_UR, fill=(0, 100, current_seconds), font=font)
        draw.text((text_x, text_y + offset), TEXT_LL, fill=(0, current_seconds, 100), font=font)
        draw.text((text_x + offset, text_y + offset), TEXT_LR, fill=(0, current_seconds, 100), font=font)

        unicornhathd.clear()
        
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                r, g, b = [int(n) for n in pixel] 
                unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

        unicornhathd.show()
        
        time.sleep(1)

except KeyboardInterrupt:
    unicornhathd.off()

