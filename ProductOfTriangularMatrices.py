"""
Requirement: Check if the product of two triangular matrices is
a triangular matrix.

Implementation: Given the order of a square matrix,
I check if both the product of two upper triangular matrices and
the product of two lower triangular matrices (having that order) is a upper/lower triangular matrix, for the general case.

Return value: If the product is a triangular matrix for both cases, then return True, else False
"""


def checkIfUpperTriangular(n):
    for i in range(0,n):
        j=0
        while j < i:
            for aux_index in range(0,n):
                if i <= aux_index <= j:
                    return False

            j += 1
    return True


def checkIfLowerTriangular(n):
    for i in range(0,n):
        j=0
        while j > i:
            for aux_index in range(0,n):
                if i >= aux_index >= j:
                    return False

            j += 1
    return True


def checkIfTriangular(n):
    return checkIfUpperTriangular(n) and checkIfLowerTriangular(n)


print(checkIfUpperTriangular(4))
