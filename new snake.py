import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
win_size = 800
win = pygame.display.set_mode((win_size, win_size))

# Установка размера и начального положения змейки
snake_size = 40
snake_pos = [[snake_size, 0]]

# Установка направления движения змейки
direction = 'RIGHT'

# Создание яблока
apple_pos = [random.randrange(0, win_size, snake_size) for _ in range(2)]

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Изменение направления движения змейки при нажатии клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Обновление позиции змейки
    if direction == 'UP':
        snake_pos.insert(0, [snake_pos[0][0], (snake_pos[0][1] - snake_size) % win_size])
    elif direction == 'DOWN':
        snake_pos.insert(0, [snake_pos[0][0], (snake_pos[0][1] + snake_size) % win_size])
    elif direction == 'LEFT':
        snake_pos.insert(0, [(snake_pos[0][0] - snake_size) % win_size, snake_pos[0][1]])
    elif direction == 'RIGHT':
        snake_pos.insert(0, [(snake_pos[0][0] + snake_size) % win_size, snake_pos[0][1]])

    # Проверка на столкновение с яблоком
    if snake_pos[0] == apple_pos:
        apple_pos = [random.randrange(0, win_size, snake_size) for _ in range(2)]
    else:
        snake_pos.pop()

    # Очистка окна
    win.fill((0, 0, 0))

    # Отрисовка сетки
    for i in range(0, win_size, snake_size):
        pygame.draw.lines(win, (125, 125, 125), True, ((i, 0), (i, win_size)), 1)
        pygame.draw.lines(win, (125, 125, 125), True, ((0, i), (win_size, i)), 1)

    # Отрисовка змейки
    for pos in snake_pos:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Отрисовка яблока
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], snake_size, snake_size))

    # Обновление окна
    pygame.display.update()

    # Задержка
    pygame.time.Clock().tick(10)
