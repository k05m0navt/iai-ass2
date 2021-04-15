from classes.Chromosome import Chromosome
from skimage.metrics import structural_similarity
import copy
import random
import time



class Population:
    def __init__(self, population_size, image_size, genes_number, mutation_rate, goal_image, poss_colors):
        self.population = []
        self.mutation_rate = mutation_rate
        self.image_size = image_size
        self.goal_image = goal_image
        self.genes_number = genes_number
        self.poss_colors = poss_colors
        self.child = Chromosome(self.image_size, self.genes_number, self.poss_colors)

        for _ in range(population_size):
            chromosome = Chromosome(image_size, genes_number, poss_colors)
            self.population.append(chromosome)

    def make_children(self):
        self.children = []
        population_size = len(self.population)

        for parent_1 in self.population:
            for parent_2 in self.population:
                self.child.genes = self.crossover(parent_1.genes, parent_2.genes)
            
                if parent_1 != parent_2:
                    self.child.choose_for_mutation(self.mutation_rate)
                
                self.child.ssim_score = 100 * structural_similarity(self.goal_image, self.child.image(), multichannel=True)
                self.children.append(copy.deepcopy(self.child))

        self.children = sorted(self.children, key=lambda x: x.ssim_score, reverse=True)

        self.population = []
        for i in range(population_size // 2):
            self.population.append(self.children[i])
            self.population.append(self.children[-1-i])

    def crossover(self, parent_1, parent_2):
        child = []
        for i in range(len(parent_1)):
            if i < len(parent_1) // 2:
                child.append(parent_1[i])
            else:
                child.append(parent_2[i])
        
        return child

