import os
import logging

LOCALE = "en_US"

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                    handlers=[logging.FileHandler(filename="info.log", mode='w'),
                    logging.StreamHandler()])

# shows result in a window using PIL Image.show
DEBUGGING = False

# reverses colors
INVERT_COLORS = True
