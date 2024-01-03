import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define game variables
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
game_over = False
level_completed = False
level = 0
score = 0

# Define snake variables
snake_size = 20
snake_speed = 10
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
snake_dx = 0
snake_dy = 0
snake_body = []

# Define apple variables
apple_size = 20
apple_x = random.randint(0, WIDTH - apple_size)
apple_y = random.randint(0, HEIGHT - apple_size)

# Define wall variables for level 2 and 3
wall_size = 20
walls = []

# Define functions
def draw_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    window.blit(rendered_text, (x, y))

def draw_snake():
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], snake_size, snake_size))

def draw_apple():
    pygame.draw.rect(window, RED, (apple_x, apple_y, apple_size, apple_size))

def draw_walls():
    for wall in walls:
        pygame.draw.rect(window, BLACK, (wall[0], wall[1], wall_size, wall_size))

def check_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + apple_size or x2 >= x1 and x2 < x1 + snake_size:
        if y1 >= y2 and y1 < y2 + apple_size or y2 >= y1 and y2 < y1 + snake_size:
            return True
    return False

def check_wall_collision():
    for wall in walls:
        if check_collision(snake_x, snake_y, wall[0], wall[1]):
            return True
    return False

def check_level_completed():
    if score >= 5 and level == 1:
        return True
    elif level == 2 or level == 3:
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            return True
        if check_wall_collision():
            return True
    return False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and not level_completed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dy != snake_size:
                    snake_dx = 0
                    snake_dy = -snake_size
                elif event.key == pygame.K_DOWN and snake_dy != -snake_size:
                    snake_dx = 0
                    snake_dy = snake_size
                elif event.key == pygame.K_LEFT and snake_dx != snake_size:
                    snake_dx = -snake_size
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx != -snake_size:
                    snake_dx = snake_size
                    snake_dy = 0

    # Update game logic
    if not game_over and not level_completed:
        snake_x += snake_dx
        snake_y += snake_dy
        snake_body.append([snake_x, snake_y])

        if len(snake_body) > score:
            del snake_body[0]

        if check_collision(snake_x, snake_y, apple_x, apple_y):
            score += 1
            apple_x = random.randint(0, WIDTH - apple_size)
            apple_y = random.randint(0, HEIGHT - apple_size)

        if check_level_completed():
            level_completed = True
            level += 1
            snake_body.clear()
            walls.clear()
            if level == 2:
                for _ in range(10):
                    wall_x = random.randint(0, WIDTH - wall_size)
                    wall_y = random.randint(0, HEIGHT - wall_size)
                    walls.append([wall_x, wall_y])
            elif level == 3:
                for _ in range(5):
                    wall_x = random.randint(0, WIDTH - wall_size)
                    wall_y = random.randint(0, HEIGHT - wall_size)
                    walls.append([wall_x, wall_y])

    # Draw game objects
    window.fill((255, 255, 255))
    if game_over:
        draw_text("Game Over", RED, WIDTH/2-100, HEIGHT/2-50)
    elif level_completed:
        draw_text(f"Level {level} Completed!", GREEN, WIDTH/2-150, HEIGHT/2-50)
    else:
        draw_snake()
        draw_apple()
        if level == 2 or level == 3:
            draw_walls()
        draw_text(f"Score: {score}", BLACK, 10, 10)

    # Update the game display
    pygame.display.update()
    clock.tick(30)

# Quit the game
pygame.quit()
