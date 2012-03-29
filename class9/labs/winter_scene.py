"""
winter_scene.py
===
Using the drawing and animation techniques we learned create an animation of snow falling.

1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Incorporate the code from multiple_objects.py to create the snow:
	a. However, in the setup, rather than use 0 for the initial y value, use a random value
	b. In the main loop, when iterating over the circles, check if the y value is greater than the window width (see screen_wrap.py)
	c. If the y value is greater... then bring the circle back up to the top
3. (INTERMEDIATE) Incorporate random lateral motion.  Try adding a unique velocity for x and y for each circle by expanding your two element list!  You can also use a dictionary if it makes more sense than a list with indexes.

"""
import pygame
import random

FRAME_RATE = 60
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "Winter Scene"
NUM_CIRCLES = 106
circles = []
velocity_y = 1
r = 1

for c in range(NUM_CIRCLES):
	circles.append([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)])

background_color = (220, 220, 220)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

while running == True:

	# stop the main loop when window is closed 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	screen.fill(background_color)
	for c in circles:
			pygame.draw.circle(screen, (248, 248, 255), (c[0],c[1]), r)
			c[1] += velocity_y
			if c[1] == WINDOW_HEIGHT:
				c[1] = 0

	# draw everything here!  this line draws a circle in the middle of the screen
	pygame.draw.circle(screen, (0, 0, 200), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)
	
	
	"""pygame.draw.ellipse(screen, (151, 2, 167), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)
	
	pygame.draw.rect(screen, (151, 2, 167), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)
	
	pygame.draw.arc(screen, (151, 2, 167), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)"""
 
	clock.tick(FRAME_RATE)
	pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
