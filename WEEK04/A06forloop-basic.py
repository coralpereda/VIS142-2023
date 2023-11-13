#
'''
this example contains all of the basic dance moves to create an animation including importing and blitting images
to use pygame, you might need to install pygame! sudo apt-get install python3-pygame or pip3 install pygame
but some distros will come with it
(ease of installation varies)
'''

import pygame
from pygame.locals import *
import random
import math

width = 600
height = 600

r1 = random.randrange(181,245)
g1 = random.randrange(181,244)
b1 = random.randrange(142,150)

x1 = random.randrange(0,width)
y1 = random.randrange(0,height)


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('drawing to file')

screen.fill((250, 200, 230))

'''
cx1 = random.randrange(10,width-10)
cy1 = random.randrange(10,height-10)
cx2 = random.randrange(10,width-10)
cy2 = random.randrange(10,height-10)
cx3 = random.randrange(10,width-10)
cy3 = random.randrange(10,height-10)
cx4 = random.randrange(10,width-10)
cy4 =  random.randrange(10, height-10)
2
pygame.draw.circle(screen, (r, g, b), (cx1, cy1), int(width / 6))
pygame.draw.circle(screen, (r, g, b), (cx2, cy2), int(width / 6))
pygame.draw.circle(screen, (r, g, b), (cx3, cy3), int(width / 6))
pygame.draw.circle(screen, (r, g, b), (cx4, cy4), int(width / 6))
'''

#For loop for circle
for i in range(0,500):
    #random rgb values
    r = random.randrange(181, 245)
    g = random.randrange(181, 244)
    b = random.randrange(142, 150)
    #random center coordinates
    cx = random.randrange(10, width - 10)
    cy = random.randrange(10, height - 10)
    pygame.draw.circle(screen, (r, g, b), (cx, cy), int(random.randrange(3,13)))

pygame.draw.polygon(screen, (r1, g1, b1), [(x1, y1), (500, 160), (300, 160)], 10)
#for num in range(50, 256):
#    pygame.draw.rect(screen, (num, 0, 0), Rect(width / 3 + num, height / 3 + num, width / 10, height / 10), 0)

pygame.display.update()
pygame.image.save(screen, "drawn.png")
pygame.display.quit()
pygame.quit()
exit()

