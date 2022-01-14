"""
Requirement: Check if a matrix from (M3(R), *) group is idempotent.
"""

def squareMatrix(matrix):
    n = len(matrix)
    result = [[0 for i in range(0,n)] for j in range(0,n)]
    for i in range(n):
        for j in range(n):
            aux_value = 0
            for aux_index in range(0, n):
                aux_value += matrix[i][aux_index] * matrix[aux_index][j]

            result[i][j] = aux_value
    return result


def checkIfIdempotent(matrix):
    return matrix == squareMatrix(matrix)


print(checkIfIdempotent([[2, -2, -4],[-1, 3, 4], [1, -2, -3]]))
print(checkIfIdempotent([[2, -2, -4],[-1, 3, 4], [1, -2, -2]]))