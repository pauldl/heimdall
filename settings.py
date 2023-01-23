import os
import logging

LOCALE = "en_US"

# WEBDAV_CALENDAR_URL = "webcal://p124-caldav.icloud.com/published/2/NTMwNDU5MDc1MzA0NTkwN1IMJzmC6b0EZx_yRqGCFW5En23MpomwMcpo9OKiW7hcxYBSu8cNMrii1jDykG6hkMb1EpeZLnd703-5ZyYx1zg"
# WEBDAV_IS_APPLE = True

WEBDAV_CALENDAR_URL = "https://outlook.office365.com/owa/calendar/01745a9bc9154a2b9cc90b415f25ef87@teamddm.com/c58953ab3cda415fb672f0ecba184c3f13778162208899419509/calendar.ics"
WEBDAV_IS_APPLE = False

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                    handlers=[logging.FileHandler(filename="info.log", mode='w'),
                    logging.StreamHandler()])

