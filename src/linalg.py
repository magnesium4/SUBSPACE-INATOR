from typing import List
import numpy as np
from numpy import linalg as LA
from scipy.linalg import null_space
from copy import deepcopy

def find_null_space(A: List[List[float]]) -> List[List[float]]:
    """
    Takes in a square matrix A and returns a basis for its null space.
    """
    return null_space(np.array(A)).tolist()


def find_eigen_vals(A: List[List[float]]) -> List[float]:
    """
    Takes in a square matrix A and returns its eigen values.
    """
    return LA.eigvals(np.array(A))


def find_eigen_basis(A: List[List[float]], x: float) -> List[List[float]]:
    """
    Takes in a square matrix A and an eigen value and returns the corresponding eigen basis.
    Precondition: x is a valid eigen value for A.
    """
    B = deepcopy(A)
    for row in B:
        for i, entry in enumerate(row):
            row[i] = entry - x
    return find_null_space(B)


def is_zero(A: List[List[float]]) -> bool:
    """
    Returns true if and only if A is the zero matrix.
    """
    for row in A:
        for entry in row:
            if entry != 0:
                return False
    return True


def find_generalized_eigen_basis(A: List[List[float]], x: float) -> List[float]:
    """
    Takes in a square matrix A and an eigen value and returns the corresponding generalized eigen basis.
    Precondition: x is a valid eigen value for A.
    """
    B = deepcopy(A)
    generalized_eigens = []
    while not is_zero(B):
        generalized_eigens.extend(find_eigen_basis(B, x))
        B = np.matmul(np.array(B), np.array(A)).tolist()


if __name__ == "__main__":
    print("hi")