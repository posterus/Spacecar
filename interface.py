#INTERFACE

import pygame, sys
from random import randint
from pygame.locals import *


#screen and display     INTERFACE
yellow = (255,255,0)
red = (220,0,0)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,205)
cyan = (32,178,170)
size = width, height = 1000,600

screen = pygame.display.set_mode(size)

#texts     INTERFACE
myfont = pygame.font.SysFont("monospace", 30, bold=True)
myfont2 = pygame.font.SysFont("monospace", 80)

#map and background       INTERFACE
karta = [0,0]
link_place = "Clock Town"
clock_town = pygame.image.load("clock_town.jpg").convert()
termina_field = pygame.image.load("termina_field.jpg").convert()
snow_head = pygame.image.load("snow_head.jpg").convert()
ikana_valley = pygame.image.load("ikana_valley.jpg").convert()
southern_swamp = pygame.image.load("southern_swamp.jpg").convert()
great_bay = pygame.image.load("great_bay.jpg").convert()

place_font = pygame.font.SysFont("monospace", 50)

#music and sound   INTERFACE
music = pygame.mixer.music.load("zelda_main_theme.mp3")
pygame.mixer.music.play(-1,0)
rupee_sound = pygame.mixer.Sound("rupee_sound.wav")
link_hurt = pygame.mixer.Sound("link_hurt.wav")
link_dead = pygame.mixer.Sound("link_dead.wav")
song_of_time = pygame.mixer.Sound("song_of_time.wav")

#moon config    INTERFACE
moon = pygame.transform.scale(pygame.image.load("moon.png"), (100,100))
moonrect = moon.get_rect()
moonrect.center = 600,50

background = clock_town

#minilink config        INTERFACE
minilink = (pygame.transform.scale(pygame.image.load("link_down.gif"), (20, 20)))
minilinkrect = minilink.get_rect()
minilinkrect_x = 905
minilinkrect_y = 465
minilinkrect.center = minilinkrect_x,minilinkrect_y

#mini ocarina config     INTERFACE
miniocarina = pygame.transform.scale(pygame.image.load("ocarina.png"), (20, 20))
miniocarinarect = miniocarina.get_rect()
miniocarinarect_x = 905
miniocarinarect_y = 465
miniocarinarect.center = (miniocarinarect_x, miniocarinarect_y)

#heart config    INTERFACE
heart = pygame.transform.scale(pygame.image.load("heart.png"), (30, 30))


def menu():
        screen.fill(black)

        startrect1 = pygame.Rect(400, 250, 200, 100)
        #startrect2 = pygame.Rect(400, 250, 200, 100)
        #startrect3 = pygame.Rect(400, 250, 200, 100)
        pygame.draw.rect(screen, red, startrect1)
        #pygame.draw.rect(screen, red, startrect2)
        #pygame.draw.rect(screen, red, startrect3)
        
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                
                        if event.type == pygame.mouse.get_pressed():
                        ## if mouse is pressed get position of cursor ##
                                pos = pygame.mouse.get_pos()
                                ## check if cursor is on button ##
                                if startrect1.collidepoint(pos):
                                    ## exit ##
                                        pygame.quit()
                                        sys.exit()
                            
                pygame.display.flip()

