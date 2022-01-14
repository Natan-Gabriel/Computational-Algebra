"""
Requirement: Check if a given matrix is Hermitian
"""

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary


def checkIfHermitian(matrix):
    for i in range(len(matrix)):
        for j in range(i+1):
            if matrix[i][j].real != matrix[j][i].real or matrix[i][j].imaginary != -matrix[j][i].imaginary:
                return False

    return True


def readComplexMatrix():
    n = int(input())
    matrix = [[None for i in range(0, n)] for j in range(0, n)]
    for i in range(n):
        for j in range(n):
            l = list(map(int, input().split(" ")))
            matrix[i][j] = ComplexNumber(l[0],l[1])
    return matrix


print(checkIfHermitian([[ComplexNumber(1,0),ComplexNumber(1,1),ComplexNumber(2,-3)],
                       [ComplexNumber(-1,1),ComplexNumber(0,0),ComplexNumber(0,4)],
                       [ComplexNumber(2,3),ComplexNumber(0,-4),ComplexNumber(3,0)]]))

print(checkIfHermitian([[ComplexNumber(1,0),ComplexNumber(1,1),ComplexNumber(2,-3)],
                       [ComplexNumber(1,-1),ComplexNumber(0,0),ComplexNumber(0,4)],
                       [ComplexNumber(2,3),ComplexNumber(0,-4),ComplexNumber(3,0)]]))