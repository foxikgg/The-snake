import os
import sys
import pygame

import level_choice_win


class Skin:
    def __init__(self, clr_snake, clr_apple):
        pygame.init()
        self.size = self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        self.background_image = pygame.image.load('data/skin_snake_and_apple_menu.png')
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # Текущие цвета
        self.color_snake = clr_snake
        self.color_apple = clr_apple

        # Позици текущих цветов
        self.color_snake_pos = [578, 77, 50, 50]
        self.color_apple_pos = [653, 77, 50, 50]

        # Позици новых цветов
        self.color_snake_pos_green = [578, 77, 50, 50]
        self.color_snake_pos_blue = [578, 77, 50, 50]
        self.color_snake_pos_white = [578, 77, 50, 50]

        self.color_apple_pos_red = [653, 77, 50, 50]
        self.color_apple_pos_yellow = [653, 77, 50, 50]
        self.color_apple_pos_blue = [653, 77, 50, 50]

        self.clock = pygame.time.Clock()
        self.running = True

    def load_image(self, name, colorkey=None):
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

    def exit_button(self):
        self.button(self.width - 70, 30, 40, 40, (0, 0, 0), '[->', 20, x_indent=12,
                    y_indent=10, font_size=30, filled=1)
        for event in pygame.event.get():
            self.Mouse_x, self.Mouse_y = pygame.mouse.get_pos()
            if (event.type == pygame.MOUSEBUTTONDOWN and self.Mouse_x in range(self.width - 70, self.width - 70 + 40)
                    and self.Mouse_y in range(30, 30 + 40)):
                self.running = False
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Обработка нажатия кнопки "Играть"
                    if (self.btn_play_pos[0] < mouse_pos[0] < self.btn_play_pos[0] + self.btn_play_pos[2] and
                            self.btn_play_pos[1] < mouse_pos[1] < self.btn_play_pos[1] + self.btn_play_pos[3]):
                        level_choice_win.Game().run()


            self.screen.blit(self.background_image, (0, 0))
            pygame.display.flip()
            self.clock.tick(50)

        pygame.quit()