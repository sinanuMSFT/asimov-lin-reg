
import numpy as np


matrix = np.array([
    [1.5,  250, 2.2,  8,  2, 460],
    [2.2,  500, 1.8, 16,  3, 880],
    [2.8, 1000, 1.5, 32,  4, 1350],
    [3.2, 2000, 1.3, 64,  5, 2000],
    [3.6, 4000, 2.0, 64,  6, 2350],
    [2.2,  500, 1.3, 16,  4, 1000],
    [4.0, 4000, 4.0, 64,  6, 2250]
])
np.set_printoptions(suppress=True, precision=2)  # suppress scientific notation, 2 decimal places
def fit_model(matrix):
    # Please write your code inside this function
    
    X = matrix[:, :-1]
    y = matrix[:, -1]
    coefficients, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
    print(coefficients)
    print(X @ coefficients)

# simulate reading a file
fit_model(matrix)