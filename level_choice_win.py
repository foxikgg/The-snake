import os
import sys
import pygame

import level_choice_win
import level1_snake
import level2_snake
import level3_snake


class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        self.background_image = pygame.image.load('data/level_menu.png')
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.btn_level1_pos = [470, 325, 393, 54]
        self.btn_level2_pos = [470, 390, 393, 54]
        self.btn_level3_pos = [470, 455, 393, 54]

        self.blue = (165, 166, 246)
        self.yellow = (255, 218, 68)
        self.green = (16, 207, 117)
        self.red = (235, 87, 87)
        self.gray = (35, 62, 84)

        self.dark = (0, 0, 0)
        self.dark_yellow = (94, 80, 23)
        self.dark_red = (158, 27, 36)
        self.dark_blue = (79, 79, 117)
        self.dark_green = (8, 105, 59)

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

    def button(self, x, y, w, h, color, text, border_raduis, x_indent=70, y_indent=10, font_size=42, filled=0):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, w, h), filled, border_radius=border_raduis)
        font = pygame.font.Font(None, font_size)
        text = font.render(text, True, (0, 0, 0))
        self.screen.blit(text, [x + (w // 2) - x_indent, y + (h // 2) - y_indent])
        return pygame.Rect(x, y, w, h)

    def exit_button(self):
        self.button(self.width - 70, 30, 40, 40, (0, 0, 0), '[->', 20, x_indent=12,
                    y_indent=10, font_size=30, filled=1)
        for event in pygame.event.get():
            self.Mouse_x, self.Mouse_y = pygame.mouse.get_pos()
            if (event.type == pygame.MOUSEBUTTONDOWN and self.Mouse_x in range(self.width - 70,
                                                                               self.width - 70 + 40) and
                    self.Mouse_y in range(30, 30 + 40)):
                self.running = False

    def main_menu(self):
        level1_button = self.button(*self.btn_level1_pos, self.green, 'Уровень 1', 30)
        level2_button = self.button(*self.btn_level2_pos, self.blue, 'Уровень 2', 30)
        level3_button = self.button(*self.btn_level3_pos, self.red, 'Уровень 3', 30)
        self.exit_button()
        return level1_button, level2_button, level3_button

    def run(self):
        level1_button, level2_button, level3_button = self.main_menu()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Обработка нажатия кнопки "Играть"
                    if (self.btn_level1_pos[0] < mouse_pos[0] < self.btn_level1_pos[0] + self.btn_level1_pos[2] and
                            self.btn_level1_pos[1] < mouse_pos[1] < self.btn_level1_pos[1] + self.btn_level1_pos[3]):
                        level1_snake.Level1().run()
                    elif (self.btn_level2_pos[0] < mouse_pos[0] < self.btn_level2_pos[0] + self.btn_level2_pos[2] and
                          self.btn_level2_pos[1] < mouse_pos[1] < self.btn_level2_pos[1] + self.btn_level2_pos[3]):
                        level2_snake.Level2().run()
                    elif (self.btn_level3_pos[0] < mouse_pos[0] < self.btn_level3_pos[0] + self.btn_level3_pos[2] and
                          self.btn_level3_pos[1] < mouse_pos[1] < self.btn_level3_pos[1] + self.btn_level3_pos[3]):
                        level3_snake.Level3().run()

            self.screen.blit(self.background_image, (0, 0))
            self.main_menu()
            pygame.display.flip()
            self.clock.tick(50)

        pygame.quit()


if __name__ == "__main__":
    Game().run()
