#
'''
this example contains all of the basic dance moves to create an animation including importing and blitting images
to use pygame, you might need to install pygame! sudo apt-get install python3-pygame or pip3 install pygame
but some distros will come with it
(ease of installation varies)
'''
import random
import pygame
from pygame.locals import *
#import math #so far we are not using the math package in this program

pygame.init()
pygame.display.set_caption('drawing to file')

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

#random colors
r = random.randrange(50,155)
g = random.randrange(50,155)
b = random.randrange(50,155)

screen.fill((0,0,0))
pygame.draw.circle(screen, (r, g, b), (width/4, height/4), int(width/6)) #int() converts

for num in range(50, 256):
    pygame.draw.rect(screen, (num, g, b), Rect(width/3 + num, height/3 + num, width/10, height/10), 0)

for i in range(0,20):
    #random values for first point of triangle
    x = random.randrange(10, width - 10)
    y = random.randrange(10 , height - 10)
    # random values for second point of triangle
    x1 = random.randrange(int(width/8), int(3*width/2))
    y1 = random.randrange(int(height/8), int(3*height/2))
    # random values f
    #     x2 = random.randrange( int(width/4), int(3*or third point of trianglewidth/4))
    y2 = random.randrange( int(height/4), int(3*height/4))
    #random value of the thickness of my stroke
    t = random.randrange(1,10)
    #variable c has a random value that will be added to the already existing r,g,b values each time the loop runs.each new color is placed in a new variable
    c = random.randrange(0,100)
    rnew = r + c
    gnew = g + c
    bnew = b + c
    #finally, draw the polygons
    pygame.draw.polygon(screen, (rnew, gnew, bnew), [(x, y), (x1, y1), (x2, y2)], t)

pygame.display.update()
pygame.image.save(screen, "A04drawn.png")
pygame.display.quit()

pygame.quit()
exit()


