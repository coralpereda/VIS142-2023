# this code is based on Brett's Stalbaum's code objects3.py for VIS142 at UCSD.
# It introduces objects in python. I have added a list of objects along other minor changes.
#please edit substantially before submitting this as an assignment

import pygame
from pygame.locals import *
from sys import exit
import math
import random

clock = pygame.time.Clock()
pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('objects!')

class Face:
    color = (15, 15, 15)
    happy = False
    locationX = 0
    locationY = 0
    expressionStart = 0
    expressionEnd = 0
    size = 50
    fill = 0
    black = (0, 0, 0)

    def __init__(self, color, happy, locationX, locationY, size):  # Face(color, happy, locationX, locationY, size)
        self.color = color
        self.happy = happy
        self.locationX = locationX
        self.locationY = locationY
        self.size = size
        if happy:
            self.expressionStart = self.degreesToRadians(180)
            self.expressionEnd = self.degreesToRadians(360)
        else:  # sad
            self.expressionStart = self.degreesToRadians(0)
            self.expressionEnd = self.degreesToRadians(180)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.locationX, self.locationY), self.size, self.fill)
        pygame.draw.circle(screen, self.black, (self.locationX - 10, self.locationY - 10), 10, 0)
        pygame.draw.circle(screen, self.black, (self.locationX + 20, self.locationY - 10), 10, 0)

        if self.happy == False:
            pygame.draw.arc(screen, self.black, (self.locationX - 20, self.locationY + 20, 40, 40),
                            self.expressionStart, self.expressionEnd, 5)
        else:
            pygame.draw.arc(screen, self.black, (self.locationX - 20, self.locationY - 10, 40, 40),
                            self.expressionStart, self.expressionEnd, 5)

    def update(self, xc, yc):
        self.locationX += xc
        self.locationY += yc

        if self.locationX > width:
            self.locationX = 0
        if self.locationY > height:
            self.locationY = 0

    # def changeMood(self):
    # Can we add features? How would we do that?
    # pass

    # degrees to radians
    def degreesToRadians(self, deg):
        return deg / 180.0 * math.pi


# self is equivalent to Face( in declaration when in a list
# make list of faces!
faces = []

# let's add 200 faces to the list and for each createe a random color and size
for i in range(0, 200):
    r = random.randrange(126, 250)
    g = random.randrange(86, 250)
    b = random.randrange(70, 156)
    lx = random.randrange(0, width)
    ly = random.randrange(0, height)
    s = random.randrange(20, 50)
    faces.append(Face((r, g, b), True, lx, ly, s))

# main animation
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    # i = 0 # this counter var is not longer needed
    for f in faces:
        xchange = random.randrange(1, 5)
        ychange = random.randrange(1, 5)
        f.draw()
        f.update(xchange, ychange)

    pygame.display.update()
    clock.tick(30)
