
import pygame, sys, random, time


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))
image = pygame.image.load(r'E:/virus.png')
image2 =pygame.image.load(r'E:/virus.png')

pygame.display.set_caption("GAME")

x = 500
y = 450
width = 20
height = 10
yv = 0
xv = 0
vel = 10
blue = [0, 0, 255]
black = (0, 0, 0)



run = True
def virus():
     if xv < 100 or xv > 700:
         yv = random.randint(0,800)
         screen.blit(image,(xv, yv))
     else:
         yv = random.randint(0,800)
         screen.blit(image, (xv, yv))
     if (xv, yv) == (x, y):
         msg("Game Over")
def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()
def msg(text):
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (400, 200)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
'''def timer(sec):
    while sec > 0:
        print(sec)
        sec-=1
        time.sleep(1)
        virus()



    if sec == 0:
        screen.fill(black)
        msg("GAME OVER")
        time.sleep(5)
        pygame.quit()
'''

while run:
    #timer(30)
    xv = random.randint(0,800)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<800-width:
        x += vel
    pygame.display.update()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, blue, (x, y, 30, 10))
    pygame.display.update()
    clock.tick(60)
