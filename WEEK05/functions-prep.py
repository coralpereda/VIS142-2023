#
'''
This code is still based on basic.py by Brett Stahlbaum used as teaching materials for the class VIS142 in the Fall 2023.
'''
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('drawing to file')

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

#random colors
r = random.randrange(50,155)
g = random.randrange(50,155)
b = random.randrange(50,155)

screen.fill((0, 0, 0))
#pygame.draw.circle(screen, (r, g, b), (width/4, height/4), int(width/6)) #int() converts

# for num in range(50, 256):
    #pygame.draw.rect(screen, (num, g, b), Rect(width/3 + num, height/3 + num, width/10, height/10), 0)

#basic function example

def triangles(maxnum):
    #triangle in the first quadrant
    # random values for first point of triangle
    for i in range(0,maxnum):
        #random values for first point of triangle
        x = random.randrange(10, width - 10)
        y = random.randrange(10 , height - 10)
        # random values for second point of triangle
        x1 = random.randrange(int(width/8), int(3*width/2))
        y1 = random.randrange(int(height/8), int(3*height/2))
        # random values for third point of triangle
        x2 = random.randrange( int(width/4), int(3*width/4))
        y2 = random.randrange( int(height/4), int(3*height/4))
        #random value of the thickness of my stroke
        t = random.randrange(1,10)
        #variable c has a random value that will be added to the already existing r,g,b values each time the loop runs.each new color is placed in a new variable
        c = random.randrange(0,100)
        rnew = r + c
        gnew = g + c
        bnew = b + c
        # finally, draw the polygons
        pygame.draw.polygon(screen, (rnew, gnew, bnew), [(x, y), (x1, y1), (x2, y2)], t)

triangles(500)


#def triQuadrants():
    #pygame.draw.polygon(screen, (rnew, gnew, bnew), [(x, y), (x1, y1), (x2, y2)], t)


pygame.display.update()
pygame.image.save(screen, "functions01.png")
pygame.display.quit()

pygame.quit()
exit()


