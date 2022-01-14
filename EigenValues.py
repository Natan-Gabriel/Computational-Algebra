import numpy as np
from sympy import symbols, Matrix, Poly

"""
Requirement: Compute the eigen values associated to a square matrix having the order 2 or 3, 
by computing its characteristic polynomial.
"""

def readSquareMatrix():
    n = int(input("Input the size of the matrix: "))

    print("Input the matrix:")
    A = [[0 for i in range(0,n)] for j in range(0,n)]

    for i in range(0, n):
        A[i] = [int(i) for i in input().strip().split(" ")]

    return np.matrix(A)


def computeEigenValuesWrapper(A):
    if len(A) <= 1 or len(A) >= 4:
        return "The matrix has to be square and to have the order 2 or 3"
    return computeEigenValues(A)


def computeEigenValues(A):
    lambda_variable = symbols('lambda')  # Turn a into a symbolic variable
    P_A = Matrix(A - lambda_variable * np.identity(len(A)))
    det = P_A.det()
    coeffs = Poly(det, lambda_variable).all_coeffs()
    eigen_values = np.roots(coeffs)

    return "The characteristic polynomial is: " + str(det) + "\nAnd the corresponding eigen values are: " + str([eigen_value for eigen_value in eigen_values])


def main():
    print(computeEigenValuesWrapper(readSquareMatrix()))


main()