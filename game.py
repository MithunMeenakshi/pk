#Initialising Pygame
import pygame, sys
import time
import random
from pygame.locals import*
pygame.init()
#display
width = 120
length = 120
screen = pygame.display.set_mode((width, length))
#Colours
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
#IMPORT IMAGE
image = pygame.image.load(r'E:/virus.png')
#variables
gameexit = pygame.QUIT

#KEYBOARD INPUT

#functions
def main():
    #KEEP IT OPEN SESAME
    running = True
    timer(15)
    while running:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
            running = False
def gameover():
    print("to play again, press KEYDOWN")
    for event in pygame.event.get():
        if event.type == pygame.K_DOWN:
            main()
def timer(sec):
    while sec > 0:
        print(sec)
        sec-=1
        time.sleep(1)
    if sec == 0:
        gameover()


#screen.blit(image, (imgx, imgy))
pygame.display.update()
main()
