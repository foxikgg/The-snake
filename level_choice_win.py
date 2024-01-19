import os
import sys
import pygame



class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        self.background_image = pygame.image.load('data/main_menu.png')
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        
        self.btn_level1_pos = [585, 450, 151, 36]
        self.btn_level2_pos = [585, 500, 151, 36]
        self.btn_level3_pos = [585, 450, 151, 36]
        
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

    def button(self, x, y, w, h, color, text, border_raduis, x_indent=40, y_indent=10, font_size=36, filled=0):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, int(y), int(w), int(h)), filled, border_radius=border_raduis)
        font = pygame.font.Font(None, font_size)
        text = font.render(text, True, (0, 0, 0))
        self.screen.blit(text, [x + (w // 2) - x_indent, y + (h // 2) - y_indent])
        return pygame.Rect(x, y, w, h)

    def exit_button(self):
        self.button(self.width - 70, 30, 40, 40, (0, 0, 0), '[->', 20, x_indent=12, y_indent=10, font_size=30, filled=1)

    def main_menu(self):
        level1_button = self.button(585, 450, 151, 36, (16, 207, 117), 'Уровень 1', 20)
        level2_button = self.button(585, 500, 151, 36, 36, (165, 166, 246), 'Уровень 2', 20)
        level3_button = self.button(585, 550, 151, 36, 36, (165, 166, 246), 'Уровень 3', 20)
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
                        pass
                    elif (self.btn_level2_pos[0] < mouse_pos[0] < self.btn_level2_pos[0] + self.btn_level2_pos[2] and
                          self.btn_level2_pos[1] < mouse_pos[1] < self.btn_level2_pos[1] + self.btn_level2_pos[3]):
                        print('Level_2()')  # Assuming Level_1 is another class like Game

            self.screen.blit(self.background_image, (0, 0))
            self.main_menu()
            pygame.display.flip()
            self.clock.tick(50)

        pygame.quit()


if __name__ == "__main__":
    Game().run()
