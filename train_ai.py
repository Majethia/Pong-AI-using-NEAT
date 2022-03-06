import pygame
import pickle
import neat
from Game import Game
from const import *

clock = pygame.time.Clock()

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        g = Game(p2_size=HEIGHT)
        run = True
        while run:
            clock.tick(FPS*3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            game_info = g.loop()
            output = net.activate((g.p1.pos.y - g.p1.size, g.p1.pos.y + g.p1.size, game_info.ball_y, game_info.distance_from_p1))
            decision = output.index(max(output))
            if decision == 0:
                g.p1.move(7.5)
            if decision == 1:
                g.p1.move(-7.5)
            if game_info.score != [0, 0]:
                genome.fitness = g.hits
                print(g.hits)
                break

def run_neat(config):
    p = neat.Population(config)
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-49')
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    return p.run(eval_genomes, 50)


if __name__ == "__main__":
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config.txt')
    best = run_neat(config)
    with open("best.pickle", "wb") as f:
        pickle.dump(best, f)

