import pygame
import pickle
import neat
from Game import Game
from const import *

clock = pygame.time.Clock()



def main():
    config1 = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config1.txt')
    config2 = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config2.txt')
    with open("best(3 input nodees).pickle", "rb") as f:
        best1 = pickle.load(f)
    with open("best(4 input nodees).pickle", "rb") as f:
        best2 = pickle.load(f)

    net1 = neat.nn.FeedForwardNetwork.create(best1, config1)
    net2 = neat.nn.FeedForwardNetwork.create(best2, config2)
    

    g = Game()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game_info = g.loop()

        #Ai for player 1
        output1 = net1.activate((g.p1.pos.y, game_info.ball_y, game_info.distance_from_p1))
        decision1 = output1.index(max(output1))
        if decision1 == 0:
            g.p1.move(7.5)
        elif decision1 == 1:
            g.p1.move(-7.5)
        
        #Controls for player 2
        # keys_pressed = pygame.key.get_pressed()

        # if keys_pressed[pygame.K_DOWN]:
        #     g.p2.move(7.5)

        # if keys_pressed[pygame.K_UP]:
        #     g.p2.move(-7.5)


        # Ai for player 2
        output2 = net2.activate((g.p2.pos.y - g.p2.size, g.p2.pos.y + g.p2.size, game_info.ball_y, game_info.distance_from_p2))
        decision2 = output2.index(max(output2))
        if decision2 == 0:
            g.p2.move(7.5)
        elif decision1 == 1:
            g.p2.move(-7.5)

main()
