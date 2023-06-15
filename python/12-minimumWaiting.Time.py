# O(nLogn) time, because of sorting algorithm
# O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0

    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft

    return totalWaitingTime

solution = minimumWaitingTime([3, 2, 1, 2, 6])
# Solution: 17
print(solution)