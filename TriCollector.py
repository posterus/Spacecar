import sys, pygame
from random import randint
from pygame.locals import *
pygame.init()

#game numbers
score = 0
life = 3
speed = 4
time = 20
places = ["Clock Town", "Termina Field", "Snow Head", "Ikana Valley",
             "Southern Swamp", "Great Bay"]
start = False

#screen and display
color = 0, 0, 0
yellow = (255,255,0)
red = (220,0,0)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,205)
cyan = (32,178,170)
size = width, height = 1000,600
screen = pygame.display.set_mode(size)

#texts
myfont = pygame.font.SysFont("monospace", 30, bold=True)
myfont2 = pygame.font.SysFont("monospace", 80)

#map and background
karta = [0,0]
link_place = "Clock Town"
clock_town = pygame.image.load("clock_town.jpg").convert()
termina_field = pygame.image.load("termina_field.jpg").convert()
snow_head = pygame.image.load("snow_head.jpg").convert()
ikana_valley = pygame.image.load("ikana_valley.jpg").convert()
southern_swamp = pygame.image.load("southern_swamp.jpg").convert()
great_bay = pygame.image.load("great_bay.jpg").convert()

place_font = pygame.font.SysFont("monospace", 50)

#moon config
moon = pygame.transform.scale(pygame.image.load("moon.png"), (100,100))
moonrect = moon.get_rect()
moonrect.center = 600,50

background = clock_town

#music and sound
music = pygame.mixer.music.load("zelda_main_theme.mp3")
pygame.mixer.music.play(-1,0)
rupee_sound = pygame.mixer.Sound("rupee_sound.wav")
link_hurt = pygame.mixer.Sound("link_hurt.wav")
link_dead = pygame.mixer.Sound("link_dead.wav")
song_of_time = pygame.mixer.Sound("song_of_time.wav")

#link config
link_x = 500
link_y = 500

scream = True
link_win = pygame.transform.scale(pygame.image.load("link_win.gif"), (200,300))
link_up = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
link_down = pygame.transform.scale(pygame.image.load("link_down.gif"), (100, 100))
link_left = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))

link = link_down
linkrect = link.get_rect()

linkrect.center = link_x, link_y

#minilink config
minilink = (pygame.transform.scale(pygame.image.load("link_down.gif"), (20, 20)))
minilinkrect = minilink.get_rect()
minilinkrect_x = 905
minilinkrect_y = 465
minilinkrect.center = minilinkrect_x,minilinkrect_y

#triforce config
tri_x = 500
tri_y = 130

triforce = pygame.transform.scale(pygame.image.load("triforce.png"), (50,50))
triforcerect = triforce.get_rect()

triforcerect.center = (tri_x, tri_y)

#mask config
mask = pygame.transform.scale(pygame.image.load("mask.png"), (100, 100))
maskrect = mask.get_rect()

#ocarina config
ocarina = pygame.transform.scale(pygame.image.load("ocarina.png"), (50, 50))
ocarinarect = ocarina.get_rect()
ocarina_x = 700
ocarina_y = 300
ocarinarect.center = (ocarina_x,ocarina_y)
oca_place = "Clock Town"

#mini ocarina config
miniocarina = pygame.transform.scale(pygame.image.load("ocarina.png"), (20, 20))
miniocarinarect = miniocarina.get_rect()
miniocarinarect_x = 905
miniocarinarect_y = 465
miniocarinarect.center = (miniocarinarect_x, miniocarinarect_y)

#heart config
heart = pygame.transform.scale(pygame.image.load("heart.png"), (30, 30))

pygame.key.set_repeat(30, 1)
clock = pygame.time.Clock()

#minimap

def minimap():
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

#menu


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

#Game loop
while 1:
        clock.tick(60)        

        for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                        #link movement
                        if keys[pygame.K_LEFT]:
                                linkrect.left -= speed
                        if keys[pygame.K_RIGHT]:
                                linkrect.left += speed
                        if keys[pygame.K_UP]:
                                linkrect.top -= speed
                        if keys[pygame.K_DOWN]:
                                linkrect.top += speed

        #link with edge
        if ((3 in (map(abs, karta)) or (sum(map(abs, karta))==4))):
                linkrect.center = [500,300]
                karta = [0,0]
                minilinkrect_x = 905
                minilinkrect_y = 465
        #move left
        elif(linkrect.right<=0):
                linkrect.right = 1100
                karta[0] -= 1
                minilinkrect_x -= 30
        #move right
        elif(linkrect.left>=1000):
                linkrect.left = -50
                karta[0] += 1
                minilinkrect_x += 30
        #move up
        elif(linkrect.bottom<=0):
                linkrect.bottom = 650
                karta[1] += 1
                minilinkrect_y -= 30
        #move down
        elif(linkrect.top>=600):
                linkrect.top = -50
                karta[1] -= 1
                minilinkrect_y += 30
                
        #place on map

        if ((3 in (map(abs, karta)) or (sum(map(abs, karta))==4))):
                background = clock_town
                link_place = "Clock Town"
        elif karta == [0,0]:
                background = clock_town
                link_place = "Clock Town"
        elif(karta[1] == 2):
                background = snow_head
                link_place = "Snow Head"
        elif(karta[0] == 2):
                background = ikana_valley
                link_place = "Ikana Valley"
        elif(karta[1] == -2):
                background = southern_swamp
                link_place = "Southern Swamp"
        elif(karta[0] == -2):
                background = great_bay
                link_place = "Great Bay"
        elif ((1 in karta) or (-1 in karta)):
                background = termina_field
                link_place = "Termina Field"
                
        #link with ocarina        
        if linkrect.colliderect(ocarinarect):
                pygame.mixer.Sound.play(song_of_time)
                time = 20 + pygame.time.get_ticks()/1000
                oca_place = places[randint(0,5)]
                ocarina_x = randint(50,950)
                ocarina_y = randint(50,550)
        if link_place == oca_place:
                ocarinarect.center = (ocarina_x,ocarina_y)
        else:
                ocarinarect.center = (-1000,0)


        #link with triforce        
        if linkrect.colliderect(triforcerect):
                pygame.mixer.Sound.play(rupee_sound)
                score+=1
                speed+=1
                while(True):
                        mask_x = randint(0,950)
                        mask_y = randint(0,550)
                        maskrect.center = (mask_x, mask_y)

                        tri_x = randint(0,950)
                        tri_y = randint(0,550)
                        triforcerect.center = (tri_x, tri_y)
                        
                        if (not(linkrect.colliderect(maskrect))
                        and not(maskrect.colliderect(triforcerect))
                        and not(linkrect.colliderect(triforcerect))):
                                break
                        
        #link with mask
        if score > 0:
                if linkrect.colliderect(maskrect):
                        life -= 1
                        if life!=0:
                                pygame.mixer.Sound.play(link_hurt)
                                
                        while(True):
                                link_x = randint(0,950)
                                link_y = randint(0,550)
                                linkrect.center = (link_x, link_y)
                                if (not(linkrect.colliderect(maskrect))):
                                        break
                                                
        time_left = time-(pygame.time.get_ticks()/1000)
        if time_left == 0:
                life = 0
        #death               
        if life == 0:
                screen.fill(black)
                moon = pygame.transform.scale(pygame.image.load("moon.png"), (1000,1000))
                moonrect = moon.get_rect()
                moonrect.center = 500,300
                screen.blit(moon,moonrect)

                if scream == True:
                        pygame.mixer.Sound.play(link_dead)
                        scream = False
                gameover_label = myfont2.render("GAME OVER",1, red)
                esc_label = myfont.render("Press ESC",1, red)
                screen.blit(gameover_label,(300,220))
                screen.blit(esc_label,(435,320))
                score_label = myfont.render("Score:" + str(score), 1, yellow)
                screen.blit(score_label, (820, 30))
        #live
        if life>0:
                screen.blit(background,[0,0])

                if time < 10:
                        moon = pygame.transform.scale(pygame.image.load("moon.png"), (100,100))
                        moonrect = moon.get_rect()
                        
                screen.blit(moon, moonrect)

                minimap()
                
                screen.blit(ocarina,ocarinarect)

                screen.blit(link, linkrect)
                screen.blit(triforce, triforcerect)
                if life >= 3:
                        screen.blit(heart, (140,30))
                if life >= 2:
                        screen.blit(heart, (90,30))
                if life >= 1:
                        screen.blit(heart, (40,30))
                if score>0:
                        screen.blit(mask, maskrect)
                
                score_label = myfont.render("Score:" + str(score), 1, yellow)
                place_label = myfont.render(link_place + " " + str(karta), 1, white)
                time_label = myfont.render("Moon crash in: "+str(time_left),1, red)
                oca_label = myfont.render("Ocarina: " + oca_place, 1, blue)
                screen.blit(score_label, (820, 30))
                screen.blit(place_label, (580,560))
                screen.blit(time_label, (200,30))
                screen.blit(oca_label, (30, 560))

                

        #50 triforce
        if score == 50:
                time = 1000000
                screen.fill(black)
                screen.blit(link_win, (400,240))
                win_label = myfont2.render("50  YOU WIN",1, yellow)
                
                screen.blit(win_label, (250,100))
                screen.blit(triforce, (370,120))
                
        pygame.display.flip()




