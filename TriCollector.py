import sys, pygame
from random import randint
from pygame.locals import *
pygame.init()

from interface import *

pygame.key.set_repeat(30, 1)
clock = pygame.time.Clock()


#game numbers    ENGINE
score = 0
#life = 3
#speed = 4
time = 20
places = ["Clock Town", "Termina Field", "Snow Head", "Ikana Valley",
             "Southern Swamp", "Great Bay"]
start = False

#link config     ENGINE

#scream = True
#link_win = pygame.transform.scale(pygame.image.load("link_win.gif"), (200,300))
#link_up = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
#link_down = pygame.transform.scale(pygame.image.load("link_down.gif"), (100, 100))
#link_left = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
#
#link = link_down
#linkrect = link.get_rect()
#
#linkrect.center = 500, 500

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

class Item:
	def __init__(self, possition, image, size):
		self.possition = possition
		self.image = image
		self.size = size

	def Render(self):
		self.item = pygame.image.load(self.image, self.size )

	def Newpossition(self, minX, minY, maxX, maxY):
		item_X = randint(self.minX, self.maxX)
		item_Y = randint(self.minY, self.maxY)
		return item_X, item_Y




class Text:
	def __init__(self, input_string, color, myfont, possition ):
		self.input_string = input_string 
		self.color  = color
		self.myfont = myfont
		self.text = 0
		self.possition = possition


	def Render(self):
		self.text = self.myfont.render(self.input_string, 1, self.color)
	
	def blit(self): 
                screen.blit(self.text, self.possition)

class Link:
	life = 3
	speed = 4	
	scream = True
	link_win = pygame.transform.scale(pygame.image.load("link_win.gif"), (200,300))
	link_up = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
	link_down = pygame.transform.scale(pygame.image.load("link_down.gif"), (100, 100))
	link_left = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
	
	link = link_down
	linkrect = link.get_rect()
	
	linkrect.center = 500, 500
	

	




class TriCollector:
	def possition_update(self, karta, linkrect,minilinkrect_x, minilinkrect_y):	
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
		return(background, link_place, minilinkrect_x, minilinkrect_y, karta)
	def gameover(self):
		screen.fill(black)
                moon = pygame.transform.scale(pygame.image.load("moon.png"), (1000,1000))
                moonrect = moon.get_rect()
                moonrect.center = width/2,height/2
                screen.blit(moon,moonrect)

                if link.scream == True:
                        pygame.mixer.Sound.play(link_dead)
                        link.scream = False
                gameover_label = myfont2.render("GAME OVER",1, red)
                esc_label = myfont.render("Press ESC",1, red)
                screen.blit(gameover_label,(300,220))
                screen.blit(esc_label,(435,320))
                score_label = myfont.render("Score:" + str(score), 1, yellow)
                screen.blit(score_label, (820, 30))

TC = TriCollector()
link = Link()

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
                                link.linkrect.left -= link.speed
                        if keys[pygame.K_RIGHT]:
                                link.linkrect.left += link.speed
                        if keys[pygame.K_UP]:
                                link.linkrect.top -= link.speed
                        if keys[pygame.K_DOWN]:
                                link.linkrect.top += link.speed
#	TC.gameloop()
	background, link_place, minilinkrect_x, minilinkrect_y, karta = TC.possition_update(karta, link.linkrect,minilinkrect_x, minilinkrect_y)	

        #link with ocarina
        if link.linkrect.colliderect(ocarinarect):
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
        if link.linkrect.colliderect(triforcerect):
                pygame.mixer.Sound.play(rupee_sound)
                score+=1
                link.speed+=1
                while(True):
                        mask_x = randint(0,width-50)
                        mask_y = randint(0,height-50)
                        maskrect.center = (mask_x, mask_y)

                        tri_x = randint(0,width-50)
                        tri_y = randint(0,height-50)
                        triforcerect.center = (tri_x, tri_y)
                        
                        if (not(link.linkrect.colliderect(maskrect))
                        and not(maskrect.colliderect(triforcerect))
                        and not(link.linkrect.colliderect(triforcerect))):
                                break
                        
        #link with mask
        if score > 0:
                if link.linkrect.colliderect(maskrect):
                        link.life -= 1
                        if link.life!=0:
                                pygame.mixer.Sound.play(link_hurt)
                                
                        while(True):
                                link_x = randint(0,width-50)
                                link_y = randint(0,height-50)
                                link.linkrect.center = (link_x, link_y)
                                if (not(link.linkrect.colliderect(maskrect))):
                                        break
                                                
        time_left = time-(pygame.time.get_ticks()/1000)
        if time_left == 0:
                link.life = 0
        
	
	#death               
        if link.life == 0:
		TC.gameover()
        #live
        if link.life>0:
                screen.blit(background,[0,0])

                if time < 10:
                        moon = pygame.transform.scale(pygame.image.load("moon.png"), (200,100))
                        moonrect = moon.get_rect()
                        
                screen.blit(moon, moonrect)

                minimap(minilinkrect, minilink,
                        minilinkrect_x, minilinkrect_y, oca_place,
                        miniocarina, miniocarinarect)
                
                screen.blit(ocarina,ocarinarect)

                screen.blit(link.link, link.linkrect)
                screen.blit(triforce, triforcerect)
                if link.life >= 3:
                        screen.blit(heart, (140,30))
                if link.life >= 2:
                        screen.blit(heart, (90,30))
                if link.life >= 1:
                        screen.blit(heart, (40,30))
                if score>0:
                        screen.blit(mask, maskrect)
       		         
		# Updating Score,  time and link/ocarina possition	
		score_label = Text("Score" + str(score), yellow, myfont, (820, 30)) 
		place_label = Text(link_place + "" + str(karta), white, myfont, (580,560))
		time_label = Text("Moon crash in: "+str(time_left), red, myfont,(200, 30))
		oca_label = Text("Ocarina: "+oca_place, blue, myfont,(30, 560))
				
		score_label.Render()
		place_label.Render()
		time_label.Render()
		oca_label.Render()

                
		score_label.blit()
		place_label.blit()
		time_label.blit()
		oca_label.blit()


        #50 triforce
        if score == 50:
                time = 1000000
                screen.fill(black)
                screen.blit(link_win, (400,240))
                win_label = myfont2.render("50  YOU WIN",1, yellow)
                
                screen.blit(win_label, (250,100))
                screen.blit(triforce, (370,120))
                
        pygame.display.flip()




