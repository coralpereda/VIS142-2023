# a hello pypng example
# note: your distro may not have pypng:
# $ pip3 install pypng
# and if you don't have pip3:
# $ sudo apt install python3-pip
# there may be other ways to install, varies by distro. Welcome to Linux!

import png
import random

# we will create a 720p size image, 1280 x 720
width = 1280
height = 720

imagedata = [] # just to show we created a list called imagedata
for h in range(height): # h is the index of the rows. each time you go down a pixel.
    row = [] # every time I go to a new row, I create a new list that will store the RGB values.
    for w in range(width):
        for val in range(0,3): # val is declared right here, it is a counter. and for every pixel you assign it three values.
            row.append(random.randrange(0,256)) # its 255 because 256 is not included. look up randrange. This will generate a random value from 0 to 255. but because it's in a for loop this will happen 3 times per pixel
        #for val in range(0,3): # val is declared right here, it is a counter. and for every pixel you assign it three values.
            #row.append(random.randrange(128,256)) # its 255 because 256 is not included. look up randrange. This will generate a random value from 0 to 255. but because it's in a for loop this will happen 3 times per pixel
    # print(row) # here we can see that the output so far is a list and not tuples. This is only one row.
    imagedata.append(row) # all of the rows are put in there.

png.from_array(imagedata, 'RGB').save("color.png") #fromarray function in the pypng library