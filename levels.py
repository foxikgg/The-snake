import pygame
import sys
import level1_snake
import level2_snake
import level3_snake



# Определение функции для создания окна уровня
def level_window(level_name):
    level_win = pygame.display.set_mode((200, 200))
    font = pygame.font.Font(None, 36)
    text = font.render(level_name, 1, (10, 10, 10))
    textpos = text.get_rect(centerx=level_win.get_width()/2)
    level_win.blit(text, textpos)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    # Check if mouse position is over the button.
                    if textpos.collidepoint(event.pos):
                        running = False
        pygame.display.update()
    pygame.quit()

# Определение функции для создания кнопки
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    flag = False

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            flag = True
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

# Определение функции для отображения текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Инициализация Pygame
pygame.init()

# Установка размеров окна
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Установка цветов
white = (255,255,255)
black = (0,0,0)
bright_red = (255,0,0)
red = (200,0,0)
bright_green = (0,255,0)
green = (0,200,0)
bright_blue = (0,0,255)
blue = (0,0,200)

# Запуск игрового цикла
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gameDisplay.fill(white)

    button("Уровень 1", 150, 450, 100, 50, green, bright_green, level1_snake.Level1.run())
    button("Уровень 2", 350, 450, 100, 50, blue, bright_blue, level2_snake.Level2.run())
    button("Уровень 3", 550, 450, 100, 50, red, bright_red, level3_snake.Level3.run())

    pygame.display.update()
