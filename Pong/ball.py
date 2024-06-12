import pygame

class Ball:
    def __init__(self, x, y, size, speed_x, speed_y):
        self.x = x
        self.y = y
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen, color):
        pygame.draw.ellipse(screen, color, (self.x, self.y, self.size, self.size))

    def reset_position(self, x, y):
        self.x = x
        self.y = y
