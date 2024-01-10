import pygame
import sys
import random

pygame.init()
win_size = 800
win = pygame.display.set_mode((800, win_size))
snake_size = 40
snake_pos = [[0, 0]]
direction = 'RIGHT'
apple_pos = [random.randrange(0, win_size, snake_size) for _ in range(2)]
mark = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
    if direction == 'UP':
        snake_pos.insert(0, [snake_pos[0][0], (snake_pos[0][1] - snake_size) % win_size])
    elif direction == 'DOWN':
        snake_pos.insert(0, [snake_pos[0][0], (snake_pos[0][1] + snake_size) % win_size])
    elif direction == 'LEFT':
        snake_pos.insert(0, [(snake_pos[0][0] - snake_size) % win_size, snake_pos[0][1]])
    elif direction == 'RIGHT':
        snake_pos.insert(0, [(snake_pos[0][0] + snake_size) % win_size, snake_pos[0][1]])
    if snake_pos[0] == apple_pos:
        apple_pos = [random.randrange(0, win_size, snake_size) for _ in range(2)]
        mark += 1
        print(f'Текущие очки: {mark}')
    else:
        snake_pos.pop()

    # Проверка на столкновение с собственным телом
    if snake_pos[0] in snake_pos[1:]:
        snake_pos = [[snake_size, 0]]
        direction = 'RIGHT'
        mark = 0

    # Очистка окна
    win.fill((0, 0, 0))

    # Отрисовка сетки
    for i in range(0, win_size, snake_size):
        pygame.draw.lines(win, (125, 125, 125), True, ((i, 0), (i, win_size)), 1)
        pygame.draw.lines(win, (125, 125, 125), True, ((0, i), (win_size, i)), 1)

    # Отрисовка змейки
    for pos in snake_pos:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pos[0], pos[1], snake_size, snake_size), border_radius=10)

    # Отрисовка яблока
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], snake_size, snake_size),
                     border_radius=50)

    pygame.display.update()

    pygame.time.Clock().tick(10)
