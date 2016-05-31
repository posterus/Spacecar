import sys, pygame
from math import *
pygame.init()

size = width, height = 800,800 
black = 0, 0, 0

screen = pygame.display.set_mode(size)
car = pygame.transform.scale(pygame.image.load("car.png"), (100, 100))
#car = pygame.image.load('car.png')
moon = pygame.transform.scale(pygame.image.load("Moon.png"), (200, 200))
pygame.key.set_repeat(60, 50)
######### MOON CONFIG #######################
x_m=400
y_m=400

mass_m = 100 #kg


####### Spaceship Config ###################
x=0
y=0
mass = 1 #kg
motor_x=0
motor_y=0

carect = car.get_rect()

def speed(x, y, x_m, mass, y_m, mass_m, motor_x, motor_y):
	F_x =(mass*mass_m)/(x-x_m)**2
	F_y =(mass*mass_m)/(y-y_m)**2
	F_x = motor_x +(((sqrt((x-x_m)**2)) / (x-x_m) )*-F_x)
	F_y = motor_y +(((sqrt((y-y_m)**2)) / (y-y_m) )*-F_x) 
	print(F_x, F_y)
	return [F_x, F_y] 

print( speed(x, y, x_m, mass, y_m, mass_m, motor_x, motor_y))

clock = pygame.time.Clock()
while 1:
	clock.tick(60)
	#keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			
			if keys[pygame.K_LEFT]:
				motor_x  -= 0.7 
			if keys[pygame.K_RIGHT]:
				motor_x += 0.7 
			if keys[pygame.K_UP]:
				motor_y -= 0.7
			if keys[pygame.K_DOWN]:
				motor_y += 0.7

	x, y = carect.center		
	#car = pygame.transform.rotate(car, tan(x/y)) 	
	screen.fill(black)
	screen.blit(moon, (x_m, y_m))
	carect = carect.move(speed(x, y, x_m, y_m, mass, mass_m, motor_x, motor_y))
	screen.blit(car, carect)
	pygame.display.flip()
	pygame.event.pump()

