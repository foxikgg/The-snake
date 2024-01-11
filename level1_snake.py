import pygame
import sys
import random

class Level1:
    def __init__(self):
        pygame.init()

        # Установка размеров окна
        self.win_size = 800
        self.win = pygame.display.set_mode((800, self.win_size))

        # Установка размера и начального положения змейки
        self.snake_size = 40
        self.snake_pos = [[0, 0]]

        # Установка направления движения змейки
        self.direction = 'RIGHT'

        # Создание яблока
        self.apple_pos = [random.randrange(0, self.win_size, self.snake_size) for _ in range(2)]
        self.mark = 0  # Количество собранных яблок

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

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

            # Отрисовка яблока
            pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(self.apple_pos[0], self.apple_pos[1], self.snake_size, self.snake_size),
                             border_radius=50)
            pygame.display.update()

            pygame.time.Clock().tick(10)  # Задержка

# Запуск игры

