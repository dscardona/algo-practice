def twoNumberSum(array, targetSum):
        for i in range(len(array) - 1):
            firstNum = array[i]
            for j in range(i + 1, len(array)):
                secondNum = array[j]
                if firstNum + secondNum == targetSum:
                    return [firstNum, secondNum]
        return []

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []