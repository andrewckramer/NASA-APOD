# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:29:30 2023

@author: Andrew Kramer
"""

import tkinter as tk
from save_image import save_image
from PIL import ImageTk

def apod_gui(text, img):

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
