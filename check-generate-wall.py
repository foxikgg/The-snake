import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button
import numpy as np
import random

def generate_matrix():
    # Изменение размера матрицы на 20x20
    matrix = np.zeros((20, 20), dtype=int)
    matrix[9][9] = 1  # Размещение змейки

    def is_valid_wall(matrix, row, col, length, is_horizontal):
        # Проверка стенок, чтобы они не ставились возле краёв матрицы
        if is_horizontal:
            if col + length > 19 or col == 0:
                return False
            if np.any(matrix[row, max(0, col-1):min(20, col + length + 1)] != 0):
                return False
        else:
            if row + length > 19 or row == 0:
                return False
            if np.any(matrix[max(0, row-1):min(20, row + length + 1), col] != 0):
                return False
        return True

    def place_wall(matrix, row, col, length, is_horizontal):
        if is_horizontal:
            matrix[row, col:col + length] = 2
        else:
            matrix[row:row + length, col] = 2

    wall_orientations = [True, False, True, False, random.choice([True, False])]
    random.shuffle(wall_orientations)

    for is_horizontal in wall_orientations:
        wall_placed = False
        while not wall_placed:
            length = random.randint(4, 7)
            row, col = random.randint(1, 18), random.randint(1, 18)
            if is_valid_wall(matrix, row, col, length, is_horizontal):
                place_wall(matrix, row, col, length, is_horizontal)
                wall_placed = True

    return matrix

print(generate_matrix())

def draw_matrix(matrix):
    fig, ax = plt.subplots()
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])
    for i in range(20):
        for j in range(20):
            if matrix[i][j] == 2:  # замените 'generate_matrix' на 'matrix'
                rect = patches.Rectangle((j, i), 1, 1, linewidth=1, edgecolor='blue', facecolor='blue')
                ax.add_patch(rect)
    plt.show()

def generate_new_field(event):
    new_matrix = generate_matrix()  # вызовите функцию здесь
    draw_matrix(new_matrix)

button_ax = plt.axes([0.8, 0.05, 0.1, 0.075])
button = Button(button_ax, 'Заново', color='red', hovercolor='blue')
button.on_clicked(generate_new_field)

generated_matrix = generate_matrix()  # вызовите функцию здесь
draw_matrix(generated_matrix)


button_ax = plt.axes([0.8, 0.05, 0.1, 0.075])
button = Button(button_ax, 'Заново', color='red', hovercolor='blue')
button.on_clicked(generate_new_field)

draw_matrix(generate_matrix)


