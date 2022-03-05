from Utils import Vector
from const import HEIGHT
import pygame

class Player:
    def __init__(self, pos: Vector, size: int, color: tuple[int]) -> None:
        self.pos = pos
        self.size = size
        self.width = 20
        self.color = color
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y - self.size, self.width, 2*self.size)

    def move(self, d: int) -> None:
        if 0 + self.size < self.pos.y + d <  HEIGHT - self.size:
            self.pos.y += d
    
    def reset(self):
        self.pos.y = HEIGHT/2

    def draw(self, screen) -> None:
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y - self.size, self.width, 2*self.size)
        pygame.draw.rect(screen, self.color, self.hitbox)