from classes.Gene import Gene
import numpy as np
import cv2
import random
import copy

class Chromosome:
    def __init__(self, image_size, genes_number, poss_colors):
        self.ssim_score = -2
        self.genes = []
        self.image_size = image_size
        self.genes_number = genes_number

        for gene_number in range(genes_number):
            gene = Gene(gene_number, image_size, poss_colors)
            self.genes.append(copy.deepcopy(gene))

    def image(self):
        image_matrix = np.full((self.image_size, self.image_size, 3), 0, np.uint8)

        for gene in self.genes:
            start_point = (gene.coords["x"], gene.coords["y"])
            end_point = (gene.coords["x"] + gene.size, gene.coords["y"] + gene.size)
            square_color = gene.color[1]
            thickness = -1

            image_matrix = cv2.rectangle(image_matrix, start_point, end_point, square_color, thickness)

        return image_matrix

    def choose_for_mutation(self, mutation_rate):
        for gene in self.genes:
            gene.mutation(mutation_rate)