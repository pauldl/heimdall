#!/usr/bin/python
import sys
import os

from waveshare_epd import epd7in5_V2
from PIL import Image
import time

wd = os.path.dirname(os.path.abspath(__file__))

try:
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()
    time.sleep(2)

    Himage = Image.open(wd + '/screen.bmp')
    epd.display(epd.getbuffer(Himage))
    time.sleep(5)

    epd.sleep()

except IOError as e:
    exit()

except KeyboardInterrupt:
    epd7in5_V2.epdconfig.module_exit()
    exit()
