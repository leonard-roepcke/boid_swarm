import display
import math
import random

class Boid():
    def __init__(self, ref_boid_handler, screen, pos=(100, 100)):
        self.ref_boid_handler = ref_boid_handler
        self.screen = screen
        self.pos = pos
        self.dir = random.randint(0, 360)
        self.speed = 1

    def update(self):
        display.display_boid(self.screen, self.pos, angle=self.dir)
        self.move()
        self.update_dir()


    def move(self):
        """Intern"""
        abs_dir = math.radians(self.dir - 90)
        self.pos = (self.pos[0] + math.cos(abs_dir) * self.speed, self.pos[1] + math.sin(abs_dir) * self.speed)

        if self.pos[0] < 0:
            self.pos = self.screen.get_width(), self.pos[1]
        elif self.pos[0] > self.screen.get_width():
            self.pos = 0, self.pos[1]

        if self.pos[1] < 0:
            self.pos = self.pos[0], self.screen.get_height()
        elif self.pos[1] > self.screen.get_height():
            self.pos = self.pos[0], 0
    
    def update_dir(self):
        """Intern"""
        boids_in_radius = self.ref_boid_handler.get_boids_in_radius(self.pos, 100)
        if len(boids_in_radius) > 0:
            avg_angle = sum(b.dir for b in boids_in_radius) / len(boids_in_radius)
            self.dir = (3*self.dir + avg_angle) / 4
        else:
            self.dir += random.randint(-10, 10)


        boids_in_radius = self.ref_boid_handler.get_boids_in_radius(self.pos, 20)
        if len(boids_in_radius) > 0:
            avg_pos_x = sum(b.pos[0] for b in boids_in_radius) / len(boids_in_radius)
            avg_pos_y = sum(b.pos[1] for b in boids_in_radius) / len(boids_in_radius)
            avg_pos = (avg_pos_x, avg_pos_y)
            self.check_boid_direction(avg_pos)

    def get_distance(self, pos):
        return math.hypot(self.pos[0] - pos[0], self.pos[1] - pos[1])

    def check_boid_direction(self, pos):
        """Intern"""
        abs_dir = math.atan2(self.pos[1] - pos[1], self.pos[0] - pos[0])
        self.dir = (self.dir*3 + math.degrees(abs_dir) + 180)/4
        if self.dir < 0:
            self.dir += 360
        elif self.dir >= 360:
            self.dir -= 360
    