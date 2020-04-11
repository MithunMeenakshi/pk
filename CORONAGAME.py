''' PLEASE MAKE SURE YOU HAVE PASTED THE CORRECT DIRECTORY OF VIRUS.PNG BEFORE RUNNING'''
'''IDEA WRITTEN AND CONCEPTUALISED BY MITHUN MEENAKSHI S'''
#Initialising everything
import pygame, sys, random, time
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
image = pygame.image.load(r'E:/virus.png')#Enter the path of Virus.png in your system
pygame.display.set_caption("SOCIAL DISTANCING - THE CORONA GAME")
#The Variables
x = 500
y = 450
width = 20
height = 10
yv = 0
xv = 0
vel = 50
blue = [0, 0, 255]
black = (0, 0, 0)
imgx=xv+225
imgy=yv+225
#Moving my virus
def virus():
    #xv = random.randint(0, 450)
    screen.blit(image, (xv, yv))
    pygame.display.update()
    logic()
    clock.tick(1)
#Making my text visible
def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()
def msg(text):
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (250, 250)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
#The logic behind the game and real life - Do not go near Corona or you'll be dead
def logic():
    if x<=imgx:
        msg("GAMEOVER")
        time.sleep(5)
        pygame.quit()
    if y<=imgy :
        msg("GAMEOVER")
        time.sleep(5)
        pygame.quit()
#the game starts here
msg("SOCIAL DISTANCING - THE CORONA GAME")
time.sleep(3)
screen.fill(black)
msg("Avoid touching the virus, and you'll win for sure")
time.sleep(2)
screen.fill(black)
#The infinite loop of life/game
run = True
while run:
    xv = random.randint(0,450)#RANDOM VALUE FOR X
    yv = random .randint(0,450)#RANDOM VALUE FOR Y
    virus()#CALLING THE function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x>0:
            x -= vel
        if keys[pygame.K_RIGHT] and x<500-width:
            x += vel
        if keys[pygame.K_UP] and y>0:
            y -= vel
        if keys[pygame.K_DOWN] and y<500-height:
            y += vel
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, blue, (x, y, 30, 10))#THE PLAYER HERE IS A RECTANGLE
        pygame.display.update()
        clock.tick(10)
