import sys, pygame
from random import randint
from pygame.locals import *
pygame.init()

#from interface import *

pygame.key.set_repeat(30, 1)
clock = pygame.time.Clock()

size = width, height = 1000,600
screen = pygame.display.set_mode(size)

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
	link_place = 'Clock Town'
	link_win = pygame.transform.scale(pygame.image.load("link_win.gif"), (200,300))
	link_up = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
	link_down = pygame.transform.scale(pygame.image.load("link_down.gif"), (100, 100))
	link_left = pygame.transform.scale(pygame.image.load("link_up.gif"), (100, 100))
	
	link = link_down
	linkrect = link.get_rect()
	
	linkrect.center = 500, 500
	
class Media:
	def __init__(self, track_url, track_type):
		self.track_type = track_type 
		self.track_url = track_url
		if(self.track_type == 'background'):
			self.track = pygame.mixer.music.load(self.track_url)
  			pygame.mixer.music.play(-1,0)
		if(self.track_type == 'effect'):
			self.track = pygame.mixer.Sound(self.track_url)

  	#rupee_sound = pygame.mixer.Sound("rupee_sound.wav")
  	#link_hurt = pygame.mixer.Sound("link_hurt.wav")
  	#link_dead = pygame.mixer.Sound("link_dead.wav")
  	#song_of_time = pygame.mixer.Sound("song_of_time.wav")
 	def play(self):
		pygame.mixer.Sound.play(self.track)
		 

class TriCollector:
	yellow = (255,255,0)
 	red = (220,0,0)
  	black = (0,0,0)
  	white = (255,255,255)
   	blue = (0,0,205)
   	cyan = (32,178,170)
  
  
   	#texts     INTERFACE
   	myfont = pygame.font.SysFont("monospace", 30, bold=True)
  	myfont2 = pygame.font.SysFont("monospace", 80)	
	
	clock_town = pygame.image.load("clock_town.jpg").convert()
	termina_field = pygame.image.load("termina_field.jpg").convert()
  	snow_head = pygame.image.load("snow_head.jpg").convert()
  	ikana_valley = pygame.image.load("ikana_valley.jpg").convert()
  	southern_swamp = pygame.image.load("southern_swamp.jpg").convert()
 	great_bay = pygame.image.load("great_bay.jpg").convert()
 
 	place_font = pygame.font.SysFont("monospace", 50)
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
	
	def minimap(self, minilinkrect,minilink,
	            minilinkrect_x, minilinkrect_y, oca_place,
	            miniocarina, miniocarinarect):
	
	        minimap1 = pygame.Rect(830, 420,150,90)
	        minimap2 = pygame.Rect(860, 390,90,150)
	
	        pygame.draw.rect(screen, self.cyan, (830, 420,150,90))
	        pygame.draw.rect(screen, self.cyan, (860, 390,90,150))
	        pygame.draw.rect(screen, self.black, (860, 420,90,90),1)
	
	        pygame.draw.rect(screen, self.black, (890,450,30,30),1)
	
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

	#########################
	#### POSSITION STUFF ####
	#########################
	karta = [0, 0]
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
			background = TC.clock_town
			link_place = "Clock Town"
		elif karta == [0,0]:
			background = TC.clock_town
			link_place = "Clock Town"
		elif(karta[1] == 2):
			background = TC.snow_head
			link_place = "Snow Head"
		elif(karta[0] == 2):
			background = TC.ikana_valley
			link_place = "Ikana Valley"
		elif(karta[1] == -2):
			background = TC.southern_swamp
			link_place = "Southern Swamp"
		elif(karta[0] == -2):
			background = TC.great_bay
			link_place = "Great Bay"
		elif ((1 in karta) or (-1 in karta)):
			background = TC.termina_field
			link_place = "Termina Field"
		return(background, link_place, minilinkrect_x, minilinkrect_y, karta)

	def gameover(self):
		screen.fill(TC.black)
                moon = pygame.transform.scale(pygame.image.load("moon.png"), (1000,1000))
                moonrect = moon.get_rect()
                moonrect.center = width/2,height/2
                screen.blit(moon,moonrect)

                if link.scream == True:
                        link_dead.play()
                        link.scream = False
		gameover_label = Text('GAME OVER', TC.red, TC.myfont2, (300, 220))
		gameover_label.Render()
		gameover_label.blit()
		
		ecs_label = Text('Press ESC', TC.red, TC.myfont, (435, 320))
		ecs_label.Render()
		ecs_label.blit()

		score_label = Text('Score:' + str(score), TC.yellow, TC.myfont, (820, 30))
		score_label.Render()
		score_label.blit()


def menu():
        choice = 0
        gameon = False
        ping =  pygame.transform.scale(pygame.image.load("triforce.png"), (30,30))
        pingrect = ping.get_rect()

        pingrect.center = (170,150)

        alt1_label = TC.myfont2.render("Start game",1,TC.yellow)
        alt2_label = TC.myfont2.render("Quit",1, TC.yellow)

        screen.blit(ping,pingrect)

        while True:
                screen.fill(TC.black)
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




TC = TriCollector()
link = Link()



# music = Media('zelda_main_theme.mp3', 'background') #TO HELL WITH THIS SONG
song_of_times = Media('song_of_time.wav', 'effect')
link_dead = Media('link_dead.wav', 'effect')
link_hurt = Media('link_hurt.wav', 'effect')
rupee_sound = Media('rupee_sound.wav', 'effect')






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
	background, link_place, minilinkrect_x, minilinkrect_y, TC.karta = TC.possition_update(TC.karta, link.linkrect,TC.minilinkrect_x, TC.minilinkrect_y)	

        #link with ocarina
        if link.linkrect.colliderect(ocarinarect):
		song_of_times.play()
                #pygame.mixer.Sound.play(song_of_time)
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
               	rupee_sound.play() 
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
                                link_hurt.play()
                                
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

                if time_left < 10:
                        TC.moon = pygame.transform.scale(TC.moon, (200, 200))

                screen.blit(TC.moon, TC.moonrect)

                TC.minimap(TC.minilinkrect, TC.minilink,
                        TC.minilinkrect_x, TC.minilinkrect_y, oca_place,
                        TC.miniocarina, TC.miniocarinarect)
                
                screen.blit(ocarina, ocarinarect)

                screen.blit(link.link, link.linkrect)
                screen.blit(triforce, triforcerect)
                if link.life >= 3:
                        screen.blit(TC.heart, (140,30))
                if link.life >= 2:
                        screen.blit(TC.heart, (90,30))
                if link.life >= 1:
                        screen.blit(TC.heart, (40,30))
                if score>0:
                        screen.blit(mask, maskrect)
       		         
		# Updating Score,  time and link/ocarina possition	
		score_label = Text("Score" + str(score), TC.yellow, TC.myfont, (820, 30)) 
		place_label = Text(link.link_place + "" + str(TC.karta), TC.white, TC.myfont, (580,560))
		time_label = Text("Moon crash in: "+str(time_left), TC.red, TC.myfont,(200, 30))
		oca_label = Text("Ocarina: "+oca_place, TC.blue, TC.myfont,(30, 560))
				
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
                screen.fill(TC.black)
                screen.blit(link_win, (400,240))
                win_label = myfont2.render("50  YOU WIN",1, TC.yellow)
                
                screen.blit(win_label, (250,100))
                screen.blit(triforce, (370,120))
                
        pygame.display.flip()




