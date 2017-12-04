import pygame

pygame.init()


class Brick:
    def __init__(self, surface, height, width, color):
        """
        :param surface: The place the brick is being drawn
        :param height: The height of the brick
        :param width: The width of the brick
        :param color: The color of the brick
        """
        self.surface = surface
        self.height = height
        self.width = width
        self.color = color

    def draw(self, x, y):
        """
        :param x: The "x" coordinate on the window
        :param y: The "y" coordinate on the window
        """
        pygame.draw.rect(self.surface, self.color, (x, y, self.width, self.height), 0)
