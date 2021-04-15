import random
import math
from numba import jit, cuda


class Gene:
    def __init__(self, gene_number, image_size, poss_colors):
        self.image_size = image_size
        self.poss_colors = poss_colors
        self.color = self.poss_colors[random.randint(0, len(self.poss_colors)-1)]
        self.set_coords()
        self.set_size()

    def set_color(self):
        self.color = self.poss_colors[random.randint(0, len(self.poss_colors)-1)]

    def set_coords(self):
        self.coords = {
            "x": random.randint(0, self.image_size-1),
            "y": random.randint(0, self.image_size-1)
        }

    def set_size(self):
        self.size = random.randint(1, self.image_size)
  
    def mutation(self, mutation_rate):
        if 100 * random.random() < mutation_rate:
            self.set_coords()
            self.set_size()
            self.set_color()
