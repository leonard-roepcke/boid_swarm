import pygame
import boid_handler
global screen_size 
screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
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

        screen.fill((0,0,0))

        boids.update()

        clock.tick(60)
        pygame.display.flip()