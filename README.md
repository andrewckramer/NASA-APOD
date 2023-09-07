# NASA-APOD
GUI for interfacing with the [NASA APOD API](https://api.nasa.gov/), displaying the description and link, and prompting the user if they would like to save the image.

## Overview
This is a simple program, designed to get the current [NASA Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) from the API and display it in a GUI. The GUI is comprised of a textbox for displaying the description and link for the image, and two buttons, yes or no, which allow the user to save the image to a folder 'apods' under the filename 'apod-YYYY-MM-DD.png' if they click the 'yes' button.

The file also creates a temporary image file named 'apod.png' within the same folder as the main script, this is utilized to display the image within the GUI.

## Dependencies
This program requires the module [Requests](https://pypi.org/project/requests/) which can be installed using the following command in the terminal:
```bash
$ python -m pip install requests
```

It also requires the module [Pillow](https://pypi.org/project/Pillow/) which can be installed using the following command in the terminal:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

It also requires a folder named 'apods' to exist within the same file as the script.

## Usage
The program is fairly simple to run, as the user only needs to run 'main.py' from the command line.
```bash
python main.py
```

## Future Updates
- As of now the GUI is fairly simple and the image section of the GUI is rather crude, with the image being fixed to a specific size within the GUI. Ideally in the future, I would like to update the GUI such that the image portion will adapt to the dimensions of the image, maintaining the GUI's fixed width and height, but altering the size of the image to fit within this size whilst keeping its dimensions.

- Include the ability to catch an error with fetching the data from the API and display it in the textbox.
