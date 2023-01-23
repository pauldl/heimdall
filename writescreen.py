#!/usr/bin/python
import sys
import os

from waveshare_epd import epd7in5_V2
from PIL import Image
import time

try:
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()

    Himage = Image.open('screen.bmp')
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    epd.sleep()

except IOError as e:
    exit()

except KeyboardInterrupt:
    epd7in5_V2.epdconfig.module_exit()
    exit()
