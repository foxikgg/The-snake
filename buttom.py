import pygame
import sys

pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета кнопок
blue = (0, 0, 255)
light_blue = (173, 216, 230)
green = (0, 255, 0)
light_green = (144, 238, 144)

# Функция для создания кнопки
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h), border_radius=10)
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h), border_radius=10)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

# Функция для создания текста
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

# Функции для действий кнопок
def skins_action():
    print("Нажата кнопка Скины")

def play_action():
    print("Нажата кнопка Играть")

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    button("Скины", 150, 450, 100, 50, blue, light_blue, skins_action)
    button("Играть", 550, 450, 100, 50, green, light_green, play_action)

    pygame.display.update()
