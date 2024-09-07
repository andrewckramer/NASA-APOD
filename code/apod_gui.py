# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:29:30 2023

@author: Andrew Kramer
"""

import customtkinter as ctk
import os

from save_image import save_image
from PIL        import Image


def apod_gui(text, img, image_url, copyright):

    # Creates the GUI
    parent = ctk.CTk()

    parent.title('APOD Test')
    parent.geometry('1250x750')

    width_base = 1250

    width, height = img.size

    
    # Creates the frame for the image and displays the image
    image_frame = ctk.CTkFrame(parent, height=750, width=width)
    image_frame.pack(side='left')

    info_frame = ctk.CTkFrame(parent, height=750, width=width_base-width)
    info_frame.pack(side='right', anchor='n')


    image = ctk.CTkImage(dark_image=img, size=(width, height))

    image_label = ctk.CTkLabel(image_frame, image=image, height=height, width=width, text='')
    image_label.pack(side='top')


    # If there is copyright information, displays it below the image
    if copyright != None:
        copyright_text = f"\u00A9 {copyright}"
        copyright_label = ctk.CTkLabel(image_frame, height=25, width=width, font=('Segoe UI', 10), text=copyright_text)
        copyright_label.pack(side='bottom', padx=5)


    # Opens up the APOD logo for displaying in the GUI
    cur_path = os.path.dirname(__file__)
    logo_path = os.path.join(cur_path, '..', 'assets', 'resized_apod_logo.png')
    logo_img = Image.open(logo_path)

    logo_width, logo_height = logo_img.size

    logo_image = ctk.CTkImage(dark_image=logo_img, size=(logo_width, logo_height))

    title_label = ctk.CTkLabel(info_frame, text='', height=100, width=logo_width, image=logo_image)
    title_label.grid(row=0, columnspan=2) 


    # Creates the textbox to display the title, description, and URL
    textbox = ctk.CTkTextbox(info_frame, width=width_base-width, height=500, wrap='word', font=('Segoe UI', 14))
    textbox.grid(row=1, columnspan=2)
    textbox.insert('0.0', text)
    textbox.configure(state='disabled')


    # Creates the save button to save the image
    save_button = ctk.CTkButton(info_frame, text='Save Image', width=width_base-width, height=50, command = lambda : save_image(image_url, parent))
    save_button.grid(row=2, columnspan=2)


    parent.mainloop()
