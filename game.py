#Initialising Pygame
import pygame, sys
import time
import random
from pygame.locals import*
pygame.init()
clock = pygame.time.Clock()

#display
width = 600
length = 600

screen = pygame.display.set_mode((width, length))
#variables
x = 30
ix = 300
iy = 500
sizec = 100
#Colours
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
#IMPORT IMAGE
image = pygame.image.load(r'E:/virus.png')


#functions
def main():
    #KEEP IT OPEN SESAME
    running = True
    timer(x)
    while running:
        for event in pygame.event.get():
            if event.key == pygame.K_LEFT:
                ix-=5
                pygame.draw.rect(screen, blue, (ix, iy, 100, 50))

            if event.type == pygame.QUIT:
                running = False
#THE TIME CODE
def timer(sec):
    while sec > 0:
        count(sec)
        clrscr()
        sec-=1
        time.sleep(1)


    if sec == 0:
        msg("GAME OVER")
        time.sleep(5)
        exit(0)
#SCREEN CLEAR
def clrscr():
    screen.fill(black)
    pygame.draw.rect(screen, blue, (ix, iy, 100, 50))

#TEXT ON screen
def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()
def msg(text):
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (400, 200)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
def count(y):
    if y == 30:
        msg("30")
    if y == 29:
        msg("29")
    if y == 28:
        msg("28")
    if y == 27:
        msg("27")
    if y == 26:
        msg("26")
    if y == 25:
        msg("25")
    if y == 24:
        msg("24")
    if y == 23:
        msg("23")
    if y == 22:
        msg("22")
    if y == 21:
        msg("21")
    if y == 20:
        msg("20")
    if y == 19:
        msg("19")
    if y == 18:
        msg("18")
    if y == 17:
        msg("17")
    if y == 16:
        msg("16")
    if y == 15:
        msg("15")
    if y == 14:
        msg("14")
    if y == 13:
        msg("13")
    if y == 12:
        msg("12")
    if y == 11:
        msg("11")
    if y == 10:
        msg("10")
    if y == 9:
        msg("9")
    if y == 8:
        msg("8")
    if y == 7:
        msg("7")
    if y == 6:
        msg("6")
    if y == 5:
        msg("5")
    if y == 4:
        msg("4")
    if y == 3:
        msg("3")
    if y == 2:
        msg("2")
    if y == 1:
        msg("1")

pygame.display.update()
clock.tick(60)
main()
