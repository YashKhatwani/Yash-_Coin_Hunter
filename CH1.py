import pygame
from pygame.locals import*

pygame.init() #initializing pygame modules

screen_width=1200
screen_height=800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Coin Hunter')

#load images in game
#sun_img= pygame.image.load('image/sun.png')
bg_img= pygame.image.load('image/bg.png')

#To make screen run all time until we press cross
run=True
while run==True:
    screen.blit(bg_img,(0,0))
    #screen.blit(sun_img,(100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#for cross button at top right corner to click and close
            run = False

    pygame.display.update()
pygame.quit() 


