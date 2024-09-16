#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:01:00 2023

@author: Andrew Kramer

Function: Obtain the NASA Astronomy Picture of the Day using the NASA APOD API
"""

import os
import requests
import urllib.request

from PIL        import Image, ExifTags
from apod_gui   import apod_gui
from dotenv     import load_dotenv

# Main APOD Function
def main():
    
    # Loads the API key from .env
    load_dotenv()
    token = os.environ.get("API_KEY")
    

    # Defines the URL with the API key and scrapes the API webpage
    URL = "https://api.nasa.gov/planetary/apod?api_key="+token
    response = requests.get(URL)
    

    # Un-comment the below statement for troubleshooting to see the response of the API
    # print(response)
    

    # Gets the data from the API and formats it into a python dict with JSON
    data = response.json()


    # Defines all the values to be sent to the text box in the GUI
    title = data['title']
    date = str(data['date'])
    image_url = data['hdurl']
    explanation_text = data['explanation']
    

    # Checks if the copyright is included in the API data and defines it if present
    if 'copyright' in data.keys():
        copyright = data['copyright']
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
    text = f'Title: {title}\n\nDate: {date}\n\nExplanation: \n\n{explanation_text}\n\nURL: \n{image_url}'
    apod_gui(text, img, image_url, copyright)

    img.close()
    
if __name__ == '__main__':
    main()
