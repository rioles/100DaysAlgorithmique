"""
minimumRewards - function that Return the minimum number of candies you need to have to distribute the candies to the children.

@ratings : children children rating value

Return   : the minimum number of candies you need to have to distribute the candies to the children

Complexity: Time - O(N), Space O(N)
"""

def minimumRewards(rating):
    rewards = [1 for k in rating]

    for i in range(1,len(rating)):
        if rating[i] > rating[i - 1]:
            rewards[i] = rewards[i - 1] + 1
        if rating[i] == rating[i - 1]:
            continue

    for j in reversed(range(0,len(array)-1)):
        if rating[j] > rating[j + 1]:
            rewards[j] = max(rewards[j], rewards[j + 1] +1)
        if rating[j] == rating[j + 1]:
            continue
    return sum(rewards)
        
