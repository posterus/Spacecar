import sys, pygame
from random import randint
from pygame.locals import *
pygame.init()

from interface import *

pygame.key.set_repeat(30, 1)
clock = pygame.time.Clock()


#game numbers    ENGINE
score = 0
life = 3
speed = 4
time = 20
places = ["Clock Town", "Termina Field", "Snow Head", "Ikana Valley",
             "Southern Swamp", "Great Bay"]
start = False

#link config     ENGINE

scream = True
link_win = pygame.transform.scale(pygame.image.load("link_win.gif"), (200,300))
link_up = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
link_down = pygame.transform.scale(pygame.image.load("link_down.gif"), (100, 100))
link_left = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))

link = link_down
linkrect = link.get_rect()

linkrect.center = 500, 500

#triforce config     ENGINE
tri_x = 500
tri_y = 130

triforce = pygame.transform.scale(pygame.image.load("triforce.png"), (50,50))
triforcerect = triforce.get_rect()

triforcerect.center = (tri_x, tri_y)

#mask config     ENGINE
mask = pygame.transform.scale(pygame.image.load("mask.png"), (100, 100))
maskrect = mask.get_rect()

#ocarina config      ENGINE
ocarina = pygame.transform.scale(pygame.image.load("ocarina.png"), (50, 50))
ocarinarect = ocarina.get_rect()
ocarina_x = 700
ocarina_y = 300
ocarinarect.center = (ocarina_x,ocarina_y)
oca_place = "Clock Town"


menu()

#######################

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
                linkrect.center = [width/2,height/2]
                karta = [0,0]
                minilinkrect_x = 905
                minilinkrect_y = 465
        #move left
        elif(linkrect.right<=0):
                linkrect.right = width+50
                karta[0] -= 1
                minilinkrect_x -= 30
        #move right
        elif(linkrect.left>=1000):
                linkrect.left = -50
                karta[0] += 1
                minilinkrect_x += 30
        #move up
        elif(linkrect.bottom<=0):
                linkrect.bottom = height+50
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
                ocarina_x = randint(50,width-50)
                ocarina_y = randint(50,height-50)
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
                        mask_x = randint(0,width-50)
                        mask_y = randint(0,height-50)
                        maskrect.center = (mask_x, mask_y)

                        tri_x = randint(0,width-50)
                        tri_y = randint(0,height-50)
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
                                link_x = randint(0,width-50)
                                link_y = randint(0,height-50)
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
                moonrect.center = width/2,height/2
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
                        moon = pygame.transform.scale(pygame.image.load("moon.png"), (200,100))
                        moonrect = moon.get_rect()
                        
                screen.blit(moon, moonrect)

                minimap(minilinkrect, minilink,
                        minilinkrect_x, minilinkrect_y, oca_place,
                        miniocarina, miniocarinarect)
                
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




