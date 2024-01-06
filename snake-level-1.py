import pygame
import sys
import random

pygame.init()

# Установка размеров окна
win_size = 800
win = pygame.display.set_mode((900, win_size))

# Установка размера и начального положения змейки
snake_size = 40
snake_pos = [[0, 0]]

# Установка направления движения змейки
direction = 'RIGHT'

# Создание яблока
apple_pos = [random.randrange(0, win_size, snake_size) for _ in range(2)]
mark = 0  # Количество собранных яблок

# Позиция кнопки
btn_again_pos = [800, 50, 100, 50]
btn_exit_pos = [800, 100, 100, 50]
btn_point_pos = [800, 0, 100, 50]

# Цвета кнопок
dark = (0, 0, 0)
blue = (165, 166, 246)
green = (16, 207, 117)
red = (235, 87, 87)

dark_red = (158, 27, 36)
dark_blue = (79, 79, 117)
dark_green = (8, 105, 59)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h), border_radius=10)
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(win, ic, (x, y, w, h), border_radius=10)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    win.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


while True:
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
        # Обработка нажатия на кнопку "Заново"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (btn_again_pos[0] < mouse_pos[0] < btn_again_pos[0] + btn_again_pos[2] and
                    btn_again_pos[1] < mouse_pos[1] < btn_again_pos[1] + btn_again_pos[3]):
                snake_pos = [[0, 0]]
                direction = 'RIGHT'
                apple_pos = [random.randrange(0, win_size, snake_size) for _ in range(2)]
                mark = 0
                print(f'Текущие очки: {mark}')

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

    # Отрисовка кнопок
    button(f"Очки: {mark}", btn_point_pos[0], btn_point_pos[1], btn_exit_pos[2], btn_exit_pos[3], dark, dark)
    button("Заново", btn_again_pos[0], btn_again_pos[1], btn_again_pos[2], btn_again_pos[3], blue, dark_blue)
    button("Выход", btn_exit_pos[0], btn_exit_pos[1], btn_exit_pos[2], btn_exit_pos[3], red, dark_red)

    pygame.display.update()

    pygame.time.Clock().tick(10)  # Задержка
