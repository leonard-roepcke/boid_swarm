import display
class Boid_handler():
    def __init__(self, screen):
        self.screen = screen

    def update(self):
        display.display_boid(self.screen, (100, 100), angle=0)