# O(w * h) time | O(w* h) space
def transposeMatrix(matrix):
    transposedMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
    return transposedMatrix

print(transposeMatrix([
    [1, 2],
    [3, 4], 
    [5, 6]]))