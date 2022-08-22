import numpy as np

def scalar_mult( arr: np.arange, num: int) -> np.arange : 
    return arr*num

# multiply matrix_line by line
def matrix_vector_mul(matrix: np.array, vector: np.array) -> np.array:
    nbOfDimension = matrix.ndim
    tempVec = np.zeros((nbOfDimension))
    for rowIdx, row in enumerate(matrix) :
        for idx, val in enumerate(row) :
            tempVec[rowIdx] += val * vector[idx]
    return tempVec

# multiply vector element by element 
def matrix_vector_mul_v2(matrix: np.array, vector: np.array) -> np.array:
    nbOfDimension = matrix.ndim
    tempVec = np.zeros((nbOfDimension))
    for vecIdx, value in enumerate(vector, start=0) :
        for rowIdx, line in enumerate(matrix) : 
            tempVec[rowIdx] += line[vecIdx] * value
    return tempVec




