import pygame
import math

points = [(-6,0),(0,25),(6,0),(0,-3.5)]
real_points = []
for dx, dy in points:
    real_points.append((dx, dy))

def rotate_point(px, py, angle):
        """Nur Intern"""
        angle_rad = math.radians(angle + 180)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        return (px * cos_a - py * sin_a, px * sin_a + py * cos_a)
    
def display_boid(screen, pos, angle=0):
    """male einen boid"""
    real_points = []
    for dx, dy in points:
        rx, ry = rotate_point(dx, dy, angle)
        real_points.append((rx + pos[0], ry + pos[1]))

    pygame.draw.polygon(screen, (255,255,255), real_points)

