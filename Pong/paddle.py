import pygame


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.score = 0

    def move(self, keys, screen_height):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < screen_height - self.height:
            self.y += self.speed

    def move_auto(self, screen_height, ball_y):
        if self.y + self.height // 2 < ball_y:
            self.y += self.speed
        elif self.y + self.height // 2 > ball_y:
            self.y -= self.speed

        if self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def reset_position(self, y):
        self.y = y
