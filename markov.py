import numpy as np


def model_markov(initial, matrix):


transition_matrix = np.array([[0.12, 0.18, 0.45, 0.25],
                              [0.04, 0.26, 0.55, 0.15],
                              [0.2,  0.35, 0.05, 0.4],
                              [0.43, 0.17, 0.28, 0.12]])

initial_vector = np.array([0.1, 0.2, 0.1, 0.6])

num_realizations = 100
