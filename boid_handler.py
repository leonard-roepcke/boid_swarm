import display
import boid
class Boid_handler():
    def __init__(self, screen):
        self.screen = screen
        boids_count = 150
        self.boids = []
        for i in range(boids_count):
            self.boids.append(boid.Boid(self.screen, (i * 20, i * 45)))

        
        

    def update(self):

        for i in self.boids:
            i.update()

