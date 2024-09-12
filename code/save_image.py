# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:29:30 2023

@author: Andrew Kramer
"""

import datetime
import os
import urllib.request

# Saves the image to a jpg file whose name consists of the date of the apod, i.e. 'apod-2023-08-10.png'
def save_image(image_url, parent):
    
    # Gets the current date in the YYYY-MM-DD format
    time = datetime.datetime.utcnow().date()
    
    # Gets the current path and writes to the folder 'apods' with a file apod-YYYY-MM-DD.png
    cur_path = os.getcwd()
    path = os.path.join(cur_path, '..', 'apods', f'apod-{time}.png')
    
    # Writes the image to the file and closes the tk window
    urllib.request.urlretrieve(
        image_url,
        path
        )
    parent.destroy()
