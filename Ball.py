import time
from Utils import Vector
from const import WIDTH, HEIGHT
from Player import Player
import pygame
import random


class Timer:
    def __init__(self, time_between=0.1):
        self.start_time = time.time()
        self.time_between = time_between

    def can_change(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

timer = Timer()


class Ball:
    def __init__(self, pos: Vector) -> None:
        self.pos = pos
        self.velocity = Vector(-10, random.randint(-5, 5))
        self.alive = True
        self.death_reason = None
        self.hitbox = pygame.Rect(self.pos.x - 20, self.pos.y - 20, 20, 20)
        self.color = (0 ,0 ,255)

    def player_collision(self, p: Player):
        if self.hitbox.colliderect(p.hitbox):
            if timer.can_change():
                self.velocity = self.velocity.negative_vector()
                ry = random.randint(-5,5)
                self.velocity += Vector(0, ry)
                return True
        return False

    def update(self, p1: Player, p2: Player) -> None:
        self.hitbox = pygame.Rect(self.pos.x - 20, self.pos.y - 20, 20, 20)
        if self.alive:
            self.pos += self.velocity
            if self.pos.x < -20:
                self.alive = False
                self.death_reason = 0
                self.velocity = Vector(0, 0)
                return

            if self.pos.x > WIDTH +20:
                self.alive = False
                self.death_reason = 1
                self.velocity = Vector(0, 0)
                return

            hit = False
            if self.player_collision(p1):
                hit = True
            self.player_collision(p2)


            if self.pos.y < 0 or self.pos.y > HEIGHT:
                self.velocity.y = -self.velocity.y
            
            return hit
    
    def reset(self):
        self.alive = True
        self.velocity = Vector(-10, random.randint(-5, 5))
        self.pos = Vector(WIDTH/2, HEIGHT/2)
    
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.hitbox)