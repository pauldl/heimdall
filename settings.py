import os
import logging

LOCALE = "en_US"

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                    handlers=[logging.FileHandler(filename="info.log", mode='w'),
                    logging.StreamHandler()])

DEBUGGING = False
