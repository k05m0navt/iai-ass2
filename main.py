from classes.GeneticAlgorithm import GeneticAlgorithm

import numpy as np
import cv2
from timeit import default_timer as timer

GOAL_IMAGE_PATH = "src_images/mikasa.jpg"
IMAGE_SIZE = 512
POPULATION_SIZE = 4
GENES_NUMBER = 32
MUTATION_RATE = 15
STOP_ALGO_RATE = 75

src_image = cv2.imread(GOAL_IMAGE_PATH)
dsize = (IMAGE_SIZE, IMAGE_SIZE)
resize_src_image = cv2.resize(src_image, dsize)
goal_image = np.asarray(resize_src_image)

cv2.imwrite('goal_image.png', resize_src_image)

start = timer()
genetic_algorithm = GeneticAlgorithm(goal_image, IMAGE_SIZE, POPULATION_SIZE, GENES_NUMBER, MUTATION_RATE, STOP_ALGO_RATE)
print("Time:", timer()-start)