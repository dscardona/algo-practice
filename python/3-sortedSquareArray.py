# my solution
def sortedSquaredArray(array):
    squared_array = []
    for num in array:
        squared_array.append(num ** 2)
    squared_array.sort()
    return squared_array


#time: O(nlogn)
#space: O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value ** 2

    sortedSquares.sort()
    return sortedSquares

# O(n) time | O(n) space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue ** 2
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue ** 2
            largerValueIdx -= 1
            
    return sortedSquares