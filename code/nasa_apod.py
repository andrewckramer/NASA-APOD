#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:01:00 2023

@author: Andrew Kramer

Function: Obtain the NASA Astronomy Picture of the Day using the NASA APOD API
"""

import requests
import os
from PIL import Image, ExifTags
import urllib.request
from apod_gui import apod_gui
from dotenv import load_dotenv

# Main APOD Function
def main():
    
    load_dotenv()
    
    token = os.environ.get("API_KEY")
    
    URL = "https://api.nasa.gov/planetary/apod?api_key="+token
    
    response = requests.get(URL)
    
    # Un-comment the below statement for troubleshooting to see the response of the API
    #print(response)
    
    # Gets the data from the API and formats it with JSON
    response_json = response.json()
    list = [response_json]
    image_url = str(list[0]['hdurl'])
    
    explanation_text = list[0]['explanation']
    url_text = list[0]['hdurl']
    
    if 'copyright' in list[0].keys():
        copyright = list[0]['copyright']
        copyright = copyright.strip()
    else:
        copyright = None
    
    # Gets the current file path and sets it for the temp .png file
    cur_path = os.path.dirname(__file__)
    path = os.path.join(cur_path, "apod.png")
    
    # Writes the image to a temporary file
    urllib.request.urlretrieve(
        image_url,
        path
        )
    
    # Opens the image and resizes it for displaying in the GUI
    img = Image.open(path)
    max_size = (725, 850)
    img.thumbnail(max_size)



    try:
        # Re-orients the image if it is flipped by img.thumbnail()
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        
        exif = img._getexif()

        if exif[orientation] == 3:
            img=img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img=img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img=img.rotate(90, expand=True)

    except (AttributeError, KeyError, IndexError, TypeError):
    # Cases where images don't have getexif
        pass

    
    # Passes the image and text to the gui
    text = f'Explanation: \n\n{explanation_text}\n\nURL: \n{url_text}'
    apod_gui(text, img, image_url, copyright)

    img.close()
    
if __name__ == '__main__':
    main()
