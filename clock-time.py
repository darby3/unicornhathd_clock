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
        current_hour = datetime.datetime.now().strftime('%I')
        current_minute = datetime.datetime.now().strftime('%M')
        current_seconds = int(datetime.datetime.now().strftime('%S')) * 2

        try:
            active_minute
        except NameError:
            active_minute = int(current_minute)
            r_value = random.randint(50, 255)
            g_value = random.randint(50, 255)
            b_value = random.randint(50, 255)

        if int(current_minute) != active_minute:
            active_minute = int(current_minute)
            if active_minute % 5 == 0:
                r_value = random.randint(50, 255)
                g_value = random.randint(50, 255)
                b_value = random.randint(50, 255)

        rgb_values = [r_value, g_value, b_value]
        fill_values = (rgb_values[0], rgb_values[1], rgb_values[2])

        TEXT_UL = current_hour[0]
        TEXT_UR = current_hour[1]
        TEXT_LL = current_minute[0]
        TEXT_LR = current_minute[1]

        image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))

        draw = ImageDraw.Draw(image)
        draw.text((text_x, text_y), TEXT_UL, fill=fill_values, font=font)
        draw.text((text_x + offset, text_y), TEXT_UR, fill=fill_values, font=font)
        draw.text((text_x, text_y + offset), TEXT_LL, fill=fill_values, font=font)
        draw.text((text_x + offset, text_y + offset), TEXT_LR, fill=fill_values, font=font)

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

