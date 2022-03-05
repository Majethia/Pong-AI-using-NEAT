import pygame
from Player import Player
from Ball import Ball
from Utils import Vector
from const import *


class Game:
    def __init__(self, p1_size = 50, p2_size = 50) -> None:
        self.hits = 0
        self.score = [0, 0]
        self.WIN = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("PONG!!")
        self.ball = Ball(Vector(WIDTH/2, HEIGHT/2))
        self.p1 = Player(Vector(0, HEIGHT/2), p1_size, (255, 0, 0))
        self.p2 = Player(Vector(WIDTH - 20, HEIGHT/2), p2_size, (255, 0, 0))
        
    def loop(self) -> None:
        self.WIN.fill((255, 255, 255))
        self.p1.draw(self.WIN)
        self.p2.draw(self.WIN)
        if self.ball.update(self.p1, self.p2):
            self.hits += 1
        self.ball.draw(self.WIN)
        if not self.ball.alive:
            self.reset()
            self.score[self.ball.death_reason] += 1
            print(self.score)
        pygame.display.update()

        return GameInfo(self)


    def reset(self) -> None:
        self.ball.reset()
        self.p1.reset()
        self.p2.reset()

class GameInfo:
    def __init__(self, game: Game) -> None:
        self.score = game.score
        self.ball_y = game.ball.pos.y
        self.distance_from_p1 = abs(game.p1.pos.x - game.ball.pos.x)
        self.distance_from_p2 = abs(game.p2.pos.x - game.ball.pos.x) 
