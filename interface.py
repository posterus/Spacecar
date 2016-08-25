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
#karta = [0,0]
#link_place = "Clock Town"
clock_town = pygame.image.load("clock_town.jpg").convert()
termina_field = pygame.image.load("termina_field.jpg").convert()
snow_head = pygame.image.load("snow_head.jpg").convert()
ikana_valley = pygame.image.load("ikana_valley.jpg").convert()
southern_swamp = pygame.image.load("southern_swamp.jpg").convert()
great_bay = pygame.image.load("great_bay.jpg").convert()

place_font = pygame.font.SysFont("monospace", 50)

#music and sound   INTERFACE
#music = pygame.mixer.music.load("zelda_main_theme.mp3")
#
#pygame.mixer.music.play(-1,0)
#
#
#rupee_sound = pygame.mixer.Sound("rupee_sound.wav")
#link_hurt = pygame.mixer.Sound("link_hurt.wav")
#link_dead = pygame.mixer.Sound("link_dead.wav")
#song_of_time = pygame.mixer.Sound("song_of_time.wav")

#pygame.mixer.music.play(-1,0)
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

#miniocarina config     INTERFACE
miniocarina = pygame.transform.scale(pygame.image.load("ocarina.png"), (20, 20))
miniocarinarect = miniocarina.get_rect()
miniocarinarect_x = 905
miniocarinarect_y = 465
miniocarinarect.center = (miniocarinarect_x, miniocarinarect_y)

#heart config    INTERFACE
heart = pygame.transform.scale(pygame.image.load("heart.png"), (30, 30))

def minimap(minilinkrect,minilink,
            minilinkrect_x, minilinkrect_y, oca_place,
            miniocarina, miniocarinarect):
        
        minimap1 = pygame.Rect(830, 420,150,90)
        minimap2 = pygame.Rect(860, 390,90,150)
        
        pygame.draw.rect(screen, cyan, (830, 420,150,90))
        pygame.draw.rect(screen, cyan, (860, 390,90,150))
        pygame.draw.rect(screen, black, (860, 420,90,90),1)

        pygame.draw.rect(screen,black, (890,450,30,30),1)

        minilinkrect.center = (minilinkrect_x, minilinkrect_y)
        screen.blit(minilink,minilinkrect)

        if(oca_place == "Clock Town"):
                miniocarinarect.center = (905, 465)
        elif(oca_place == "Termina Field"):
                miniocarinarect.center = (905, 435)
        elif(oca_place == "Snow Head"):
                miniocarinarect.center = (905, 405)
        elif(oca_place == "Ikana Valley"):
                miniocarinarect.center = (965, 465)
        elif(oca_place == "Southern Swamp"):
                miniocarinarect.center = (905, 525)
        elif(oca_place == "Great Bay"):
                miniocarinarect.center = (845, 465)

        screen.blit(miniocarina,miniocarinarect)

def menu():
        choice = 0
        gameon = False
        ping =  pygame.transform.scale(pygame.image.load("triforce.png"), (30,30))
        pingrect = ping.get_rect()

        pingrect.center = (170,150)

        alt1_label = myfont2.render("Start game",1,yellow)
        alt2_label = myfont2.render("Quit",1,yellow)
        
        screen.blit(ping,pingrect)
            
        while True:
                screen.fill(black)
                screen.blit(alt1_label, (200,100))
                screen.blit(alt2_label,(200,300))
                screen.blit(ping,pingrect)
                
                for event in pygame.event.get():
                        keys = pygame.key.get_pressed()
                        if event.type == pygame.KEYDOWN:
                                
                                if event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                elif keys[pygame.K_DOWN]:
                                        pingrect.center = (170,350)
                                        choice = 1
                                elif keys[pygame.K_UP]:
                                        choice = 0
                                        pingrect.center = (170,150)
                                elif event.key == pygame.K_SPACE:
                                        if choice == 1:
                                                pygame.quit()
                                                sys.exit()
                                        elif choice == 0:
                                                gameon = True

                pygame.display.flip()
                if gameon==True:
                        break
                        
