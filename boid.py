
# --- Gewichtungen für die Boid-Kräfte ---
SEPARATION_WEIGHT = 5.5  # Trennung
ALIGNMENT_WEIGHT = 3    # Ausrichtung
COHESION_WEIGHT = 0.8     # Zusammenhalt

import display
import math
import random

class Boid():
    def __init__(self, ref_boid_handler, screen, pos=(100, 100)):
        self.ref_boid_handler = ref_boid_handler
        self.screen = screen
        self.pos = pos
        self.dir = random.randint(0, 360)
        self.speed = 5

    def update(self):
        display.display_boid(self.screen, self.pos, angle=self.dir)
        self.move()
        self.update_dir()


    def move(self):
        """Intern"""
        abs_dir = math.radians(self.dir)
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
        # --- Vektoren für die drei Regeln initialisieren ---
        cohesion_vector = [0, 0]
        separation_vector = [0, 0]
        alignment_vector = [0, 0]
        
        perception_radius = 100
        separation_radius = 25
        
        neighbors = self.ref_boid_handler.get_boids_in_radius(self.pos, perception_radius)
        
        # Entferne den Boid selbst aus der Nachbarliste
        neighbors = [b for b in neighbors if b is not self]
        
        if len(neighbors) > 0:
            # --- 1. Zusammenhalt (Cohesion) ---
            # Steuere in Richtung des Zentrums der lokalen Schwarmkameraden
            avg_pos_x = sum(b.pos[0] for b in neighbors) / len(neighbors)
            avg_pos_y = sum(b.pos[1] for b in neighbors) / len(neighbors)
            cohesion_vector = [avg_pos_x - self.pos[0], avg_pos_y - self.pos[1]]

            # --- 2. Ausrichtung (Alignment) ---
            # Steuere in die gleiche Richtung wie die lokalen Schwarmkameraden
            avg_dir_x = sum(math.cos(math.radians(b.dir)) for b in neighbors)
            avg_dir_y = sum(math.sin(math.radians(b.dir)) for b in neighbors)
            alignment_vector = [avg_dir_x, avg_dir_y]

            # --- 3. Trennung (Separation) ---
            # Vermeide das Zusammenstoßen mit lokalen Schwarmkameraden
            close_neighbors = [b for b in neighbors if self.get_distance(b.pos) < separation_radius]
            if len(close_neighbors) > 0:
                for b in close_neighbors:
                    diff_x = self.pos[0] - b.pos[0]
                    diff_y = self.pos[1] - b.pos[1]
                    separation_vector[0] += diff_x
                    separation_vector[1] += diff_y

        # --- Kombiniere die Vektoren und berechne die neue Richtung ---
        # Gewichtung der Kräfte
        final_vector_x = (
            COHESION_WEIGHT * cohesion_vector[0]
            + SEPARATION_WEIGHT * separation_vector[0]
            + ALIGNMENT_WEIGHT * alignment_vector[0]
        )
        final_vector_y = (
            COHESION_WEIGHT * cohesion_vector[1]
            + SEPARATION_WEIGHT * separation_vector[1]
            + ALIGNMENT_WEIGHT * alignment_vector[1]
        )

        if final_vector_x != 0 or final_vector_y != 0:
            target_dir = math.degrees(math.atan2(final_vector_y, final_vector_x))
            
            # Korrigierte sanfte Drehung
            # Berechne den kürzesten Winkel zwischen aktueller und Zielrichtung
            angle_diff = target_dir - self.dir
            if angle_diff > 180:
                angle_diff -= 360
            if angle_diff < -180:
                angle_diff += 360
            
            # Wende einen kleineren Bruchteil der Drehung an, um die Drehung stärker zu dämpfen
            turn_speed = 0.08  # Weniger als vorher für sanftere Drehung
            self.dir += angle_diff * turn_speed
        else:
            # Wenn keine Nachbarn da sind, behalte die aktuelle Richtung bei
            pass

        # Normalisiere den Winkel
        if self.dir < 0:
            self.dir += 360
        elif self.dir >= 360:
            self.dir -= 360

    def get_distance(self, pos):
        return math.hypot(self.pos[0] - pos[0], self.pos[1] - pos[1])
