import pygame
import time
import random

# Initialize pygame 
pygame.init()

# Set up the screen

width = 800
height = 600
block_size = 20

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0 , 0)
red = (255, 0, 0)

# Create Snake and apple 
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display ,black , [x[0],x[1], block_size,block_size])
        
def message(msg,color):
    mesg = font_style.render(msg,True, color)
    display.blit(mesg, [width/6, height/3])    
    
def gameloop():
    game_over = False
    game_close = False
    
    x = width / 2 
    y = height / 2
    
    x_change = 0
    y_change = 0
    
    snake_list = []
    length_of_snake = 1
    
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
    
    while not game_over:
        
        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q to Quit or C to play Again", red)
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        
                    if event.key == pygame.K_c:
                        gameloop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0
                    
        if x >= width or x < 0 or y >= height or y < 0:
           game_close = True
           
        x += x_change  
        y += y_change
        
        display.fill(white)
        pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
            
        for each_segment in snake_list[:-1]:
                if each_segment == snake_head:
                    game_close = True
        
        snake(block_size, snake_list)
        
        pygame.display.update()
        
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1
                    
        pygame.display.update()
        
        pygame.time.Clock().tick(snake_speed)
        
    pygame.quit()
    quit()
    
gameloop()                




"""
    Initialization: Pygame is initialized, and necessary variables are defined, including the screen dimensions, block size, and colors.

Game Setup: The game screen is set up using Pygame's display functionality. The caption for the game window is set.

Function Definitions: Two functions are defined:

snake: Draws the snake on the screen using rectangles.
message: Renders a message on the screen, typically used for displaying game over or other messages.
Main Game Loop: The gameloop function is defined, which serves as the main game loop. Inside this loop, the game progresses until either the player loses or chooses to quit.

Game Logic:

The snake's movement is controlled by arrow key inputs from the player.
If the snake collides with the boundaries of the screen or itself, the game ends.
The snake grows when it eats the "food" (red rectangle) on the screen.
Event Handling: The game handles events such as key presses to control the snake's movement and window close events.

Rendering: The game constantly updates the display to reflect changes in the game state, such as the snake's movement, the appearance of food, and the game over screen.

Game Over: When the game ends, the player is presented with a message indicating whether they won or lost. They can choose to quit the game or play again.

Game Termination: The game terminates when the player either chooses to quit or closes the game window.


"""