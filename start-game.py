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


pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('data/main_menu.png')
background_image = pygame.transform.scale(background_image, (width, height))
all_sprites = pygame.sprite.Group()


class Button:
    def __init__(self, x, y, w, h, color, text, border_raduis, x_indent=40, y_indent=10, font_size=36, filled=0):
        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h), filled, border_radius=border_raduis)
        font = pygame.font.Font(None, font_size)
        text = font.render(text, True, (0, 0, 0))
        screen.blit(text, [x + (w // 2) - x_indent, y + (h // 2) - y_indent])


class ExitButton(Button):
    def __init__(self):
        super(ExitButton, self).__init__(width - 70, 70, 40, 40, (0, 0, 0), '[->', 20, x_indent=12, y_indent=10,
                                         font_size=30, filled=1)


# цвет для кнопки Играть 16,207,117
# цвет для кнопки Скины 165,166,246

class MainMenu:
    def __init__(self):
        # button("Уровень 1", 150, 450, 100, 50, (16, 207, 117), (16, 150, 100), MainMenu.kill())
        Button(width // 2 - 100, 450, 220, 60, (16, 207, 117), 'Играть', 20)
        ExitButton()


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


dragon = AnimatedSprite(load_image("анимка.png"), 4, 2, 100, 60)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.blit(background_image, (0, 0))
    MainMenu()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
