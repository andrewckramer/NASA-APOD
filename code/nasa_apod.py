#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:01:00 2023

@author: Andrew Kramer

Function: Obtain the NASA Astronomy Picture of the Day using the NASA APOD API
"""
import requests
import os
from PIL import Image, ImageTk
import urllib.request
from dotenv import load_dotenv
from save_image import save_image
import tkinter as tk

# Main APOD Function
def main():
    
    load_dotenv()
    
    token = os.environ.get("api_key")
    
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
    
    
    # Gets the current file path and sets it for the temp .png file
    cur_path = os.path.dirname(__file__)
    path = cur_path+"/apod.png"
    
    # Writes the image to a temporary file
    urllib.request.urlretrieve(
        image_url,
        path
        )
    
    # Opens the image and resizes it for displaying in the GUI
    img = Image.open(path)
    max_size = (400, 800)
    img.thumbnail(max_size)
    
    text = f'Explanation: \n\n{explanation_text}\n\nURL: \n{url_text}'
    
    # Creates the GUI
    parent = tk.Tk()
    parent.geometry("700x875")
    parent.title("NASA APOD")

    image_frame = tk.Frame(parent, height=400, width=800)
    image_frame.pack(side=tk.TOP)
    
    # Displays the image inside the gui
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(image_frame, image = photo, height=400, width=800)
    label.pack(expand = tk.YES)
    
    # Writes the explanation and URL to a text box in the GUI
    text_box = tk.Text(parent)
    text_box.pack()
    text_box.insert(tk.END, text)
    text_box.config(state=tk.DISABLED)
    
    # Labels and buttons for saving the image if the user chooses
    label_text = tk.Label(text='Do you want to save the image?', height=2, font=(12))
    label_text.pack()
    
    yes_button = tk.Button(text='Yes', height=2, command = lambda : save_image(image_url, parent))
    yes_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    no_button = tk.Button(text='No', height=2, command = lambda : parent.destroy())
    no_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    
    parent.mainloop()
    
    img.close()
    
if __name__ == '__main__':
    main()
