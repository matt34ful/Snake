import pygame
import sys
import random

# Initalize Pygame
pygame.init()

# Constants

WIDTH, HEIGHT = 640, 480
GRID_SIZE= 20
GRID_WIDTH= WIDTH // GRID_SIZE
GRID_HEIGHT= HEIGHT // GRID_SIZE
SNAKE_SPEED= 10

#Colors

WHITE= (255,255,255)
GREEN= (0,255,0)
RED= (255,0,0)
BLACK= (0,0,0)

#Initalize the screen

screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initaialize the Clock

clock= pygame.time.Clock()

#Initalize the snake

snake= [(GRID_WIDTH //2, GRID_HEIGHT //2)]
snake_direction =(1,0)

#Initalize the Food

food= (random.randint(0, GRID_WIDTH -1), random.randint(0, GRID_HEIGHT -1))

# Initalize the score
score= 0

# Initalize the Font
font = pygame.font.Font(None, 36)

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction= (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction= (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction= (1, 0)
    
    
    #Move the Snake
    
    new_head= (snake[0][0] + snake_direction [0], snake [0][1] + snake_direction [1])
    snake.insert(0, new_head)
    
    # Check for Collision with food
    if snake[0] == food:
        score += 1 
        food = (random.randint(0, GRID_WIDTH -1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()
        
    # Check for collision with walls or itself
    if(
      snake[0][0] <0
      or snake[0][0] >= GRID_WIDTH
      or snake[0][1] < 0
      or snake[0][1] >= GRID_HEIGHT
      or snake[0] in snake[1:]
    ):
        pygame.quit()
        sys.exit()
    
    #Clear the Screen
    screen.fill(WHITE)
    
    #Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment [0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    #Draw the Food
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food [1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    # Draw the score
    draw_score(score)
    
    #Update the Display
    pygame.display.flip()
    
    #Control The Game Speed
    clock.tick(SNAKE_SPEED)
    

