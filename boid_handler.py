import display
import boid
import random
class Boid_handler():
    def __init__(self, screen):
        self.screen = screen
        boids_count = 300
        self.boids = []
        for i in range(boids_count):
            self.boids.append(boid.Boid(self, self.screen, (random.randint(0, 1920), random.randint(0, 1080))))
    
    def update(self):

        for i in self.boids:
            i.update()

    def get_boids_in_radius(self, pos, radius):
        boids_in_radius = []
        for i in self.boids:
            if i.get_distance(pos) < radius:
                boids_in_radius.append(i)
        return boids_in_radius
    
        