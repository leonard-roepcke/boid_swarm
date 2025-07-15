import pygame
import boid_handler

pygame.init()
info = pygame.display.Info()

# Vollbild, rahmenlos
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)
boids = boid_handler.Boid_handler(screen)
pygame.display.set_caption("Boid Swarm")
clock = pygame.time.Clock()

def main_loop():
    running = True
    i = 0
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        screen.fill((0,0,0, 0))

        boids.update()

        clock.tick(60)
        pygame.display.flip()