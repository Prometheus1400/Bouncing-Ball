import pygame
from Bouncing_Ball import Ball
#
#====================
screensize = 2000
ball_radius = 25
red = (255,0,0)
black = (0,0,0)
gravity = 200
run = True
#====================

# initialize pygame and screen size
pygame.init()
gameDisplay = pygame.display.set_mode((screensize,screensize))

# initialize Ball class =============
circle = Ball(ball_radius,red,gravity)
circle.set_position(screensize)
#====================================

last_key_pressed = None
while run == True:
    events = pygame.event.get()
    for event in events:
        # runs if x (to close window) has been pressed
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            last_key_pressed = event.key
            circle.user_input(last_key_pressed)
    #incrementally moves the circle.
    circle.move(pygame.time.get_ticks())
    #clears old drawings
    gameDisplay.fill(black)
    #draws new circle
    circle.draw(gameDisplay)
    pygame.display.update()
    print(circle.new_y)
