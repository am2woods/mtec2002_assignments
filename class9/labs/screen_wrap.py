"""
screen_wrap.py
===
Move the circle from top to bottom, but when it reaches the bottom, change the circle's x and y coordinates so that it starts at the top again.

1. Copy the boilerplate code from the template exercise - hello_pygame.py.
2. Rewrite the top to bottom animation code.
3. Write a conditional in the while loop that checks if the circle is at the bottom of the screen.
4. Make the radius of the circle into a variable, and use it to augment your boundary conditions for the bottom of the screen
"""

import pygame
import random

FRAME_RATE = 60
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "Dropping Balls"

background_color = (0, 99, 99)
running = True
pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

x = WINDOW_WIDTH / 2
y = 0
velocity_y = 1
velocity_x = 0

while running == True:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	screen.fill(background_color)

	# draw everything here!  this line draws a circle in the middle of the screen
	pygame.draw.circle(screen, (0, 0, 200), (x, y), 10)
	y += velocity_y
	velocity_x = random.randint(-1, 1)
	x += velocity_x
	
	if y == WINDOW_HEIGHT:
		y = 0
		
	"""pygame.draw.ellipse(screen, (151, 2, 167), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)
	
	pygame.draw.rect(screen, (151, 2, 167), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)
	
	pygame.draw.arc(screen, (151, 2, 167), (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), 10)"""
 
	clock.tick(FRAME_RATE)
	pygame.display.flip()

# exit when we're done with the loop
pygame.quit()
