import display
import math
class Boid():
    def __init__(self, screen, pos=(100, 100)):
        self.screen = screen
        self.pos = pos
        self.dir = 90
        self.speed = 1

    def update(self):
        display.display_boid(self.screen, self.pos, angle=self.dir)
        self.move()

    def move(self):
        """Intern"""
        abs_dir = math.radians(self.dir - 90)
        self.pos = (self.pos[0] + math.cos(abs_dir) * self.speed, self.pos[1] + math.sin(abs_dir) * self.speed)
