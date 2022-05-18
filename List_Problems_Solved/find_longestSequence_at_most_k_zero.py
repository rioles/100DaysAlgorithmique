"""
findLongestSequence - function that return the maximum sequence of continuous 1’s formed by replacing at-most `k` zeroes by ones

@array: array givening
@k    : number of zero accepted
Return: maximum sequence of continuous 1’s formed by replacing at-most `k` zeroes by ones

technique using : slide window

complexity: Time O(N), Space 0(1)
"""

def findLongestSequence(array, k):
    left = 0
    right = 0
    counterOfZero = 0
    maximumOneWithAtMostKZero = 0
    while right < len(array):
        if array[right] == 0:
            counterOfZero += 1
        while conterOfZero > k:
            if array[left] == 0:
                countOfZero -= 1
            left += 1
        maximumOneWithAtMostKZero = max(maximumOneWithAtMostKZero, right - left + 1)
        right += 1
    return maximumOneWithAtMostKZero
