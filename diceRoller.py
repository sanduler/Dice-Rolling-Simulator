# Ruben Sanduleac
# November 28th, 2020
# Dice Roller using python, includes a GUI

import tkinter
from PIL import Image
from PIL import ImageTk
import random



# main window of the app, top level widget which shows the window
root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Roller in Python')

# keep the window open and call the mainloop of Tk
root.mainloop()

# Adds the label into the frame
blankLine = tkinter.Label(root, text="")
blankLine.pack()

# adds a label with different font and formating
labelHeading  = tkinter.Label(root, text=
"Start the Symulation",
    fg = "light green",
        bg = "dark green",
            font = "Helvetica 16 bold italic")
labelHeading.pack()

# add the images from the main dirrectory
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# simulate the dice with random integers between 0 and 6 and generate an image for the user
dicePicture = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# create the label for the image
labelImage = tkinter.Label(root, image=dicePicture)
labelImage.image = dicePicture

# pack the widnget in the parent widget
labelImage.pack(expand=True)