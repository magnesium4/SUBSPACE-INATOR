from typing import List
import numpy as np
from numpy import linalg as LA
from scipy.linalg import null_space
from copy import deepcopy
from sympy import Matrix

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


# TODO: not sure if it works
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
    return generalized_eigens


# TODO: not sure if it works
def find_jordan_basis(A: List[List[float]]) -> List[List[float]]:
    """
    Takes in a square matrix A and returns its jordan basis.
    """
    eigens = find_eigen_vals(A)
    basis = []
    for e in eigens:
        B = deepcopy(A)
        generalized_eigens = []
        while not is_zero(B):
            generalized_eigens.append(find_eigen_basis(B, x))
            B = np.matmul(np.array(B), np.array(A)).tolist()
    

def find_jordan_form(A: List[List[float]]) -> List[List[float]]:
    """
    Returns the Jordan form of a matrix A
    """
    m = Matrix(np.array(A))
    return(np.array(m.jordan_form()[1]).tolist())


def count_inv_subspace(A: List[List[float]]) -> int:
    """
    Returns the number of invariant subspaces (jordan blocks) in A
    """
    J = find_jordan_form(A)
    ans = 1
    for i in range(1, len(J)):
        if J[i - 1][i] == 0:
            ans += 1
    return ans

if __name__ == "__main__":
    print(find_jordan_form([[5, 4, 2, 1], [0, 1, -1, -1], [-1, -1, 3, 0], [1, 1, -1, 2]]))
    print(count_inv_subspace([[5, 4, 2, 1], [0, 1, -1, -1], [-1, -1, 3, 0], [1, 1, -1, 2]]))