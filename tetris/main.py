import random
import copy
from pstats import count_calls

import pygame
from numpy.ma.core import count
from pygame.examples.go_over_there import clock

pygame.init()

columns = 11
strings = 21
screen_x = 250
screen_y = 500
fps = 30

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Tetris CODE")
clock = pygame.time.Clock()
cell_x = screen_x / (columns - 1)
cell_y = screen_y / (strings - 1)

grid = [[[1, pygame.Rect(i * cell_x, j * cell_y, cell_x, cell_y), pygame.Color("Gray")] for j in range(strings)] for i in range(columns)]

details = [
    [[-2,0], [-1,0], [0,0], [1,0]],
    [[-1,1], [-1,0], [0,0], [1,0]],
    [[1,1], [-1,0], [0,0], [1,0]],
    [[-1,1], [0,1], [0,0], [-1,0]],
    [[1,0], [1, 1], [0, 0], [-1, 0]],
    [[0, 1], [-1,0], [0, 0], [1, 0]],
    [[-1, 1], [0, 1], [0, 0], [1, 0]],
]

det = [[], [], [], [], [], [], []]

for i in range(len(details)):
    for j in range(4):
        det[i].append(pygame.Rect(details[i][j][0] * cell_x + cell_x * (columns//2), details[i][j][1] * cell_y, cell_x, cell_y))

detail = pygame.Rect(0, 0, cell_x, cell_y)
det_choice = copy.deepcopy(random.choice(det))
count = 0
game = True
rotate = False

while game:
    delta_x = 0
    delta_y = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -1
            elif event.key == pygame.K_RIGHT:
                delta_x = 1
            elif event.key == pygame.K_UP:
                rotate = True

    key = pygame.key.get_pressed()

    if key[pygame.K_DOWN]:
        count = 31 * fps

    screen.fill(pygame.Color(222, 248, 116, 100))

    for i in range(columns):
        for j in range(strings):
            pygame.draw.rect(screen, grid[i][j][2], grid[i][j][1], grid[i][j][0])

    for i in range(4):
        if ((det_choice[i].x + delta_x * cell_x < 0) or (det_choice[i].x + delta_x * cell_x >= screen_x)):
            delta_x = 0
        if ((det_choice[i].y + cell_y >= screen_y) or (grid[int(det_choice[i].x // cell_x)][int(det_choice[i].y // cell_y)+1][0]==0)):
            delta_y = 0
        for i in range(4):
            x = int(det_choice[i].x // cell_x)
            y = int(det_choice[i].y // cell_y)
            grid[x][y][0] = 0
            grid[x][y][2] = pygame.Color(45, 109, 234, 100)
        detail.x = 0
        detail.y = 0
        det_choice = copy.deepcopy(random.choice(det))

    for i in range(4): det_choice[i].x += delta_x * cell_x

    count += fps

    if count > 30 * fps:
        for i in range(4): det_choice[i].y += delta_y * cell_y
        count = 0

    for i in range(4):
        detail.x = det_choice[i].x
        detail.y = det_choice[i].y
        pygame.draw.rect(screen, pygame.Color("White"), detail)

    C = det_choice[2]
    if rotate:
        for i in range(4):
            x = det_choice[i].y - C.y
            y = det_choice[i].x - C.x
            det_choice[i].x = C.x - x
            det_choice[i].y = C.y + y
        rotate = False

    for j in range(strings - 1, -1, -1):
        count_cells = 0
        for i in range(columns):
            if grid[i][j][0] == 0: count_cells +=1
            elif grid[i][j][0] == 1: break
        if count_cells == (columns - 1):
            for l in range(columns): grid[l][0][0] = 1
            for k in range(j, -1, -1): grid[l][k][0] = grid[l][k - 1][0]

    pygame.display.flip()
    clock.tick(fps)