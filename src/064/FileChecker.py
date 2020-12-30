# -*- coding: utf-8 -*-
"""
Created 7-8-20 03:00 PM
Edited Last: 7-8-20 03:00 PM

@author: JS
"""


#Imports our required modules
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    #Set Format for displaying path
    #Default Path
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #Defining own path
    path = "C:/Users/jstov/Downloads"

    #Initialize logging event handler
    event_handler = LoggingEventHandler()

    #Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    #Start the Observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()