import pygame
import random

# initialize pygame
pygame.init()

# set screen size
screen_size = (600, 600)

# set snake block size
block_size = 20

# set colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# create game screen
screen = pygame.display.set_mode(screen_size)

# set game title
pygame.display.set_caption("Snake")

# create snake
snake = [(200, 200), (210, 200), (220, 200)]

# set initial direction
direction = "RIGHT"
change_to = direction

# create apple
apple = (random.randint(0, 29) * block_size, random.randint(0, 29) * block_size)

# set game over flag
game_over = False

while not game_over:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # check for direction change
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # move snake
    if direction == "UP":
        snake[0] = (snake[0][0], snake[0][1] - block_size)
    if direction == "DOWN":
        snake[0] = (snake[0][0], snake[0][1] + block_size)
    if direction == "LEFT":
        snake[0] = (snake[0][0] - block_size, snake[0][1])
    if direction == "RIGHT":
        snake[0] = (snake[0][0] + block_size, snake[0][1])

    # check for game over
    if snake[0][0] < 0 or snake[0][0] >= screen_size[0] or snake[0][1] < 0 or snake[0][1] >= screen_size[1]:
        game_over = True
    for block in snake[1:]:
        if block == snake[0]:
            game_over = True

    # check for apple collision
   
