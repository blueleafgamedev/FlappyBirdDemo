import pygame
from pygame.locals import *
import random

#Initialize pygame
pygame.init()

clock = pygame.time.Clock()
fps = 60

#Screen constants
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

#Screen size and window caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

#Define game variables
ground_scroll = 0
scroll_speed = 4

#Load images and store them in variables
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

#Sprite or character creation
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        #Iterate through flappy bird images
        for num in range(1, 4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]     
        self.rect = self.image.get_rect() #rectangle to hold sprite for collision detection
        self.rect.center = [x, y] #location/coordinates for sprite on screen

    def update(self):
        #Handle the animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

#Creation of a bird group for the bird class. This keeps track of the sprites added to it
bird_group = pygame.sprite.Group()

#Flappy variable and placement of flappy bird character on screen
flappy = Bird(100, SCREEN_HEIGHT/2)

bird_group.add(flappy) #Adding sprite to bird group of sprites, it is similar to a list in python

#Gameplay variable and start of game loop
gameplay = True
while gameplay:

    clock.tick(fps)

    #Draw background
    screen.blit(bg, (0,0))

    #Draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    #Draw in Flappy Bird
    bird_group.draw(screen)
    bird_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameplay = False

    pygame.display.update()
                   
pygame.quit()