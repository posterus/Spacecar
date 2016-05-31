import sys, pygame

pygame.init()

size = width, height = 620, 440
black = 0, 0, 0

screen = pygame.display.set_mode(size)
car = pygame.transform.scale(pygame.image.load("car.png"), (100, 100))
moon = pygame.transform.scale(pygame.image.load("Moon.png"), (200, 200))
pygame.key.set_repeat(50, 50)
######### MOON CONFIG #######################
x_m=100
y_m=100

mass = 40 #kg


####### Spaceship Config ###################
x=0
y=0
	
while 1:
	#keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			
			if keys[pygame.K_LEFT]:
				x  -= 7 
				#spaceship = pygame.transform.rotate(spaceship, 0)  
			if keys[pygame.K_RIGHT]:
				x += 7
				#spaceship = pygame.transform.rotate(spaceship, 90)  	
			if keys[pygame.K_UP]:
				y -= 7
			if keys[pygame.K_DOWN]:
				y += 7
				
	 	
	screen.fill(black)
	screen.blit(moon, (x_m, y_m))
	screen.blit(car, car.speed(x, y))
	pygame.display.flip()
	pygame.event.pump()
 

class spaceship():
	def location():
		return 0
	
	
	def speed():
		return [x, y]

