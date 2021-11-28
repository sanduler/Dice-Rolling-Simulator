# Ruben Sanduleac
# November 28th, 2020
# Dice Roller using python, uses the tkinter and PIL library for the GUI
# the programcreates the window where labels are create and external dice images are imported. 
# the random library is used to cycle through the images to randomly stop at image. The user inities the program 
# by pressing the 'roll' button.

import tkinter
from PIL import Image
from PIL import ImageTk
import random

# main window of the app, top level widget which shows the window
root = tkinter.Tk()
root.geometry('500x500')
root.title('Ruben Sanduleac: Dice Roller')

# Adds the label into the frame
blankLine = tkinter.Label(root, text="")
blankLine.pack()

# adds a label with different font and formating
labelHeading  = tkinter.Label(root, text="Start the Symulation", fg = "Black", font = "Times 24 bold italic")
labelHeading.pack()

# add the images from the main directory
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# simulate the dice with random integers between 0 and 6 and generate an image for the user
dicePicture = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# create the label for the image
labelImage = tkinter.Label(root, image=dicePicture)
labelImage.image = dicePicture

# packing a widget in the parent widget 
labelImage.pack(expand=True)

# function updates the image while keeping the reference during the roll
def rollDice():
    dicePicture = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    labelImage.configure(image=dicePicture)
    # keep a reference
    labelImage.image = dicePicture

# adds a button upon the users press to roll the fice
button = tkinter.Button(root, text='Roll', fg='black', command=rollDice)

# pack a widget in the parent widget
button.pack( expand=True)

# keep the window open and call the mainloop of Tk
root.mainloop()