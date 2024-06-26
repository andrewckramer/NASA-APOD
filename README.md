# NASA APOD GUI
GUI for interfacing with the [NASA APOD API](https://api.nasa.gov/), displaying the description and link, and prompting the user if they would like to save the image.

## Overview
This is a simple program, designed to get the current [NASA Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) from the API and display it in a GUI. The GUI is comprised of a textbox for displaying the description and link for the image, and a singular button, "Save Image', which allow the user to save the image to a folder 'apods' under the filename 'apod-YYYY-MM-DD.png' if they click it.

The file also creates a temporary image file named 'apod.png' within the same folder as the main script, this is utilized to display the image within the GUI.

## Dependencies
This program requires the module [Requests](https://pypi.org/project/requests/) which can be installed using the following command in the terminal:
```bash
python -m pip install requests
```

It also requires the module [Pillow](https://pypi.org/project/Pillow/) which can be installed using the following command in the terminal:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

It also requires the module [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) which can be installed using the following command in the terminal:
```bash
pip3 install customtkinter
```

It also requires a folder named 'apods' and 'assets' with the APOD logo in a file named 'resized_apod_logo.png' to exist within the same directory, but not folder as the script.

## Usage
The program is fairly simple to run, as the user only needs to run 'nasa_apod.py' from the command line.
```bash
python nasa_apod.py
```

## Recent Updates

- Made updates to the GUI where is resizes the image and keeps the aspect ratio for proper displaying.

- Fixed an image display issue, where the image would flip in the GUI but not the file.

- Made major updates to the GUI appearance, including a more graphical appearance which now features the APOD logo, now built using CustomTkinter instead of Tkinter.

- Now displays the copyright for the image if it is provided by the API.


## Future Updates

- Include the ability to catch an error with fetching the data from the API and display it in the textbox.
