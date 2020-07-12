"""
Created 7-9-20 02:20 PM
Edited Last: 7-12-20 09:00 AM

@author: JS
"""


import os
import shutil
import time
from datetime import datetime


dir1 = 'C:/Users/jstov/OneDrive/Documents'
dir2 = 'C:/Users/jstov/OneDrive/Pictures'
dir3 = 'C:/Users/jstov/OneDrive/Software'


while(True):
    def moveto(dst):
        return lambda src: shutil.move(src, dst)


    action = {
        'pdf': moveto(dir1),
        'docx': moveto(dir1),
        'csv': moveto(dir1),
        'txt': moveto(dir1),
        'exe': moveto(dir3),
        'msi': moveto(dir3),
        'msu': moveto(dir3),
        'jpg': moveto(dir2),
        '.tiff': moveto(dir2),
        'png': moveto(dir2),
        'torrent': os.remove,
    }


    src_dir = 'C:/Users/jstov/Downloads'
    for file in os.listdir(src_dir):
        ext = os.path.splitext(file)[1][1:]
        if ext in action:
            action[ext](os.path.join(src_dir, file))
    time.sleep(25)