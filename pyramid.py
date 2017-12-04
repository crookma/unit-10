# By: Magnus Crooke, File Name: pyramid.py, Last modified: 12-1-17, This program has a pyramis shaped-
# breaker game layout
import brick
import pygame
import sys
from pygame.locals import *

pygame.init()

mainSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Brick Pyramid")

EMERALD = (63, 195, 128)
WHITE = (255, 255, 255)
CASCADE = (149, 165, 166)
BURNTORANGE = (211, 84, 0)
SUNGLO = (226, 106, 106)
JAFFA = (235, 151, 78)

mainSurface.fill(WHITE)

Whitespace = 5
Redbricks = 9
getwidth = mainSurface.get_width()
Brickspace = (Whitespace * Redbricks - Whitespace)
WIDTH = (getwidth - Brickspace) / Redbricks

# This draws the fitst layer of bricks
brick_x = 0
brick_y = 375
for x in range(9):
    onebrick = brick.Brick(mainSurface, 20, WIDTH, BURNTORANGE)
    onebrick.draw(brick_x, brick_y)
    brick_x = brick_x + Whitespace + WIDTH

# This draws the second layer of bricks
brick_x = Whitespace + WIDTH
brick_y = 355 - Whitespace
for x in range(7):
    twobrick = brick.Brick(mainSurface, 20, WIDTH, SUNGLO)
    twobrick.draw(brick_x, brick_y)
    brick_x = brick_x + Whitespace + WIDTH

# This draws the third layer of bricks
brick_x = Whitespace + WIDTH + WIDTH + Whitespace
brick_y = 330 - Whitespace
for x in range(5):
    twobrick = brick.Brick(mainSurface, 20, WIDTH, JAFFA)
    twobrick.draw(brick_x, brick_y)
    brick_x = brick_x + Whitespace + WIDTH

# This draws the fourth layer of bricks
brick_x = Whitespace + Whitespace + Whitespace + WIDTH + WIDTH + WIDTH
brick_y = 305 - Whitespace
for x in range(3):
    twobrick = brick.Brick(mainSurface, 20, WIDTH, CASCADE)
    twobrick.draw(brick_x, brick_y)
    brick_x = brick_x + Whitespace + WIDTH

# This draws the fifth and last layer of bricks
brick_x = Whitespace + Whitespace + Whitespace + Whitespace + WIDTH + WIDTH + WIDTH + WIDTH
brick_y = 280 - Whitespace
for x in range(1):
    twobrick = brick.Brick(mainSurface, 20, WIDTH, EMERALD)
    twobrick.draw(brick_x, brick_y)
    brick_x = brick_x + Whitespace + WIDTH

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
