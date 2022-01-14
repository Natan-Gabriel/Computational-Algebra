from math import sqrt

import numpy as np
from sympy import symbols, Matrix, Poly, real_roots, CRootOf, Rational

"""
Requirement: Find the Galois group associated to a polynomial of order 3 or 4.
"""

def findGaloisGroup(coeffs, K = None):
    dicriminant = findPolynomialDiscriminant(coeffs)
    if len(coeffs) == 4:
        if 0 <= dicriminant == int(sqrt(dicriminant) + 0.5) ** 2:
            return "A_3"
        else:
            return "S_3"
    elif len(coeffs) == 5:
        is_square = False
        if 0 <= dicriminant == int(sqrt(dicriminant) + 0.5) ** 2:
            is_square = True

        a1 = coeffs[1]
        a2 = coeffs[2]
        a3 = coeffs[3]
        a4 = coeffs[4]

        f1_coeffs = [1, -a2, a1 * a3 - 4 * a4, -a4 * (a1 ** 2 - 4 * a2)]
        status = zerosInK(f1_coeffs, K)

        if not is_square and status == 0:
            return "S_4"
        elif is_square and status == 0:
            return "A_4"
        elif not is_square and status >= 1:
            return "B_4'"
        elif is_square and status == 2:
            return "B_4"
    else:
        return "Invalid polynomial"


def findPolynomialDiscriminant(coeffs):
    coeffs_order = len(coeffs) - 1

    coeffs_deriv = [coeff_deriv for coeff_deriv in np.polyder(coeffs)]
    coeffs_deriv_order = len(coeffs_deriv) - 1

    R = []
    R_order = coeffs_order + coeffs_deriv_order

    for index in range(0, R_order):
        if index + len(coeffs) <= R_order:
            R.append([0] * index + coeffs + [0] * (R_order - index - len(coeffs)))
        else:
            R.append([0] * (index - coeffs_deriv_order) + coeffs_deriv + [0] * (R_order - index - 1))

    det = Matrix(R).det()

    return int(((-1) ** (coeffs_order * (coeffs_order - 1) / 2) * det) / coeffs[0])


"""
return an integer (status)
if no zero of the given polynomial is in K => return 0
else if all zeros of the given polynomial are in K => return 2
else: return 1
"""
def zerosInK(coeffs, K):
    x = symbols('x')
    zeros = real_roots(Poly(coeffs,x))
    if K == "C":
        return 2
    elif K == "R":
        count = 0
        for zero in zeros:
            if not isinstance(zero,CRootOf):
                count += 1
        if count == 0:
            return 0
        if count == len(zeros):
            return 2
        else:
            return 1
    elif K == "Q":
        count = 0
        for zero in zeros:
            if isinstance(zero,Rational):
                count += 1
        if count == 0:
            return 0
        if count == len(zeros):
            return 2
        else:
            return 1


def readPolynomialFromKeyboard():
    return [int(i) for i in input("Input the coefficients of the polynomial, separated by a space: ").strip().split(" ")]


def main():
    print(findGaloisGroup([1, 1, -2, -1]))
    print(findGaloisGroup([1, 0, -1, 1]))
    print(findGaloisGroup([1, 0, 0, 0, -2],"Q"))
    print(findGaloisGroup([1, 0, 0, 0, -2], "R"))
    print(findGaloisGroup([1, 0, 0, 0, -2], "C"))

    # polynomial = readPolynomialFromKeyboard()
    #
    # K = None
    # if len(polynomial) == 5:
    #     K = input("Input K: ")
    #
    # print(findGaloisGroup(polynomial, K))


main()