#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


import feedparser
import time


feeds = [
    'https://www.nhk.or.jp/rss/news/cat0.xml',
    'https://www.nhk.or.jp/rss/news/cat1.xml',
    'https://www.nhk.or.jp/rss/news/cat3.xml',
    'https://www.nhk.or.jp/rss/news/cat4.xml',
    'https://www.nhk.or.jp/rss/news/cat5.xml',
    'https://www.nhk.or.jp/rss/news/cat6.xml',
    'https://www.nhk.or.jp/rss/news/cat7.xml',
    'https://www.nhk.or.jp/rss/news/cat2.xml'
]


# ####################
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import adafruit_ssd1306
import board
import digitalio


OLED_WIDTH   =  128
OLED_HEIGHT  =  64
DEFAULT_FONT  =  '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE     =  14

jpfont = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D8)
oled_reset = digitalio.DigitalInOut(board.D24)
oled_dc = digitalio.DigitalInOut(board.D23)

disp = adafruit_ssd1306.SSD1306_SPI(OLED_WIDTH, OLED_HEIGHT, spi, oled_dc, oled_reset, oled_cs)
disp.fill(0)
disp.show()


def draw_gyou(gyou):
    global jpfont
    global disp

    image = Image.new("1", (OLED_WIDTH, OLED_HEIGHT), 0)
    draw = ImageDraw.Draw(image)
    for i, j in enumerate(gyou):
        draw.text((0,16 * i), j, font=jpfont, fill=1)
    disp.image(image)
    disp.show()
# ####################


def main():
    for f in feeds:
        d = feedparser.parse(f)

        for entry in d.entries:
            n1 = 9
            s1 = entry.title + ' ' + entry.summary
            l1 = [s1[i:i+n1] for i in range(0,len(s1), n1)]
            n2 = 4
            l2 = [l1[i:i+n2] for i in range(0,len(l1), n2)]
            for l in l2:
                draw_gyou(l)
                time.sleep(6)

if __name__ == "__main__":
    main()
