#Initialising Pygame
import pygame
from pygame.locals import*
pygame.init()
#display
width=1200
length=1200
screen = pygame.display.set_mode((width, length))
pygame.display.update()
#Keep it open Sesame
running = True
while running:
  for event in pygame.event.get():
      #We need kuzhis for playing Pallanguzhi. So here we go
      pygame.draw.circle(screen, (255,255,255), (200,200), 50, 1)

      if event.type == pygame.QUIT:
        running = False
