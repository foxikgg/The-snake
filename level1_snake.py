import pygame
import sys
import random
import os


import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 500, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Level1:
    def __init__(self):
        pygame.init()

        # Установка размеров окна
        self.win_size = 800
        self.win = pygame.display.set_mode((1280, self.win_size))

        # Установка размера и начального положения змейки
        self.snake_size = 40
        self.snake_pos = [[0, 0]]

        self.btn_again_pos = [800, 50, 100, 50]  # Позиция кнопки "Заново"
        self.btn_point_pos = [800, 0, 100, 50]  # Позиция кнопки с отображением очков

        self.dark = (0, 0, 0)
        self.blue = (165, 166, 246)
        self.green = (16, 207, 117)
        self.red = (235, 87, 87)

        self.dark_red = (158, 27, 36)
        self.dark_blue = (79, 79, 117)
        self.dark_green = (8, 105, 59)

        # Установка направления движения змейки
        self.direction = 'RIGHT'

        # Создание яблока
        self.apple_pos = [random.randrange(0, self.win_size, self.snake_size) for _ in range(2)]
        self.mark = 0  # Количество собранных яблок

        self.dragon = AnimatedSprite(load_image("анимка.png"), 4, 2, 0, 0)


    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.win, ac, (x, y, w, h), border_radius=10)
        else:
            pygame.draw.rect(self.win, ic, (x, y, w, h), border_radius=10)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.win.blit(textSurf, textRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Изменение направления движения змейки при нажатии клавиш
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Обработка нажатия кнопки "Заново"
                    if (self.btn_again_pos[0] < mouse_pos[0] < self.btn_again_pos[0] + self.btn_again_pos[2] and
                            self.btn_again_pos[1] < mouse_pos[1] < self.btn_again_pos[1] + self.btn_again_pos[3]):
                        Level1().run()

            # Обновление позиции змейки
            if self.direction == 'UP':
                self.snake_pos.insert(0, [self.snake_pos[0][0], (self.snake_pos[0][1] - self.snake_size) % self.win_size])
            elif self.direction == 'DOWN':
                self.snake_pos.insert(0, [self.snake_pos[0][0], (self.snake_pos[0][1] + self.snake_size) % self.win_size])
            elif self.direction == 'LEFT':
                self.snake_pos.insert(0, [(self.snake_pos[0][0] - self.snake_size) % self.win_size, self.snake_pos[0][1]])
            elif self.direction == 'RIGHT':
                self.snake_pos.insert(0, [(self.snake_pos[0][0] + self.snake_size) % self.win_size, self.snake_pos[0][1]])

            # Проверка на столкновение с яблоком
            if self.snake_pos[0] == self.apple_pos:
                self.apple_pos = [random.randrange(0, self.win_size, self.snake_size) for _ in range(2)]
                self.mark += 1
                print(f'Текущие очки: {self.mark}')
            else:
                self.snake_pos.pop()

            # Проверка на столкновение с собственным телом
            if self.snake_pos[0] in self.snake_pos[1:]:
                self.snake_pos = [[self.snake_size, 0]]
                self.direction = 'RIGHT'
                self.mark = 0

            # Очистка окна
            self.win.fill((0, 0, 0))

            # Отрисовка сетки
            for i in range(0, self.win_size, self.snake_size):
                pygame.draw.lines(self.win, (125, 125, 125), True, ((i, 0), (i, self.win_size)), 1)
                pygame.draw.lines(self.win, (125, 125, 125), True, ((0, i), (self.win_size, i)), 1)

            # Отрисовка змейки
            for pos in self.snake_pos:
                pygame.draw.rect(self.win, (0, 255, 0), pygame.Rect(pos[0], pos[1], self.snake_size, self.snake_size), border_radius=10)

            # Отрисовка кнопок
            self.button("Заново", *self.btn_again_pos, self.dark, self.blue)
            self.button("Очки: " + str(len(self.snake_pos) - 1), *self.btn_point_pos, self.dark, self.green)

            # Отрисовка яблока
            pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(self.apple_pos[0], self.apple_pos[1], self.snake_size, self.snake_size),
                             border_radius=50)
            pygame.display.update()

            pygame.time.Clock().tick(10)  # Задержка

# Запуск игры

