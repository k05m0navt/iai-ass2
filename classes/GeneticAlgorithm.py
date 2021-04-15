from classes.Population import Population
from classes.Chromosome import Chromosome
import matplotlib.pyplot as plt
import cv2
import time
import numpy as np
from PIL import Image
from multiprocessing import Pool

class GeneticAlgorithm:
    def __init__(self, goal_image, image_size, population_size, genes_number, mutation_rate, stop_algo_rate):
        result = np.full((image_size, image_size, 3), 0, np.uint8)
        for i in range(image_size ** 2 // 64):
            self.algo(goal_image, image_size, population_size, genes_number, mutation_rate, stop_algo_rate, result, i)

    def algo(self, goal_image, image_size, population_size, genes_number, mutation_rate, stop_algo_rate, result, i):
        FRAGMENT_SIZE = 8
        x_s = (i % (image_size // FRAGMENT_SIZE)) * FRAGMENT_SIZE
        x_e = x_s + FRAGMENT_SIZE
        y_s = (i // (image_size // FRAGMENT_SIZE)) * FRAGMENT_SIZE
        y_e = y_s + FRAGMENT_SIZE
        goal_image_fragment = goal_image[y_s:y_e, x_s:x_e]
        gen_image = cv2.cvtColor(goal_image_fragment, cv2.COLOR_BGR2RGB)
        cv2.imwrite('fragment.png', goal_image_fragment)

        im = Image.open('fragment.png')
        im_rgb = im.convert('RGB')
        poss_colors = im_rgb.getcolors(maxcolors=10000000)

        ssim_score = -200

        iteration = 0
        population = Population(population_size, 8, genes_number, mutation_rate, goal_image_fragment, poss_colors)

        while ssim_score < stop_algo_rate and iteration < 1000:
            print("{} {} SSIM: {}".format(i, iteration, ssim_score))

            iteration += 1
            population.make_children()
            population.population = sorted(population.population, key=lambda x: x.ssim_score, reverse=True)
            ssim_score = population.population[0].ssim_score

            result[y_s:y_e, x_s:x_e] = population.population[0].image()
            gen_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
            cv2.imwrite('output_image.png', gen_image)
            gen_image = cv2.cvtColor(population.population[0].image(), cv2.COLOR_BGR2RGB)
            cv2.imwrite('output_fragment_image.png', gen_image)