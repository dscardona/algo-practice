# O(nlogn) time | O(1) constant space

def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0
    
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1



{
  "coins": [5, 6, 1, 1, 2, 3, 4, 9]
}


nonConstructibleChange(coins)