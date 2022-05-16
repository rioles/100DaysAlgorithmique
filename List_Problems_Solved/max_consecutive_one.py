"""
maxConsecutiveOnes - function that return maximumConsecuitive one
@array: List of binary number ( 0 or 1)
Return: return the maximum consecutive one

solution 1
time complexity = 0(N)
space complexity = 0(1)
"""
def maxConsecutiveOnes(array):
    counterOne = 0
    counter = 0
    maximumConsecutiveOne = float("-inf")
    while counter < len(array):
        counterOne += 1
        if array[counter] == 0:
            counterOne = 0
        maximumConsecutiveOne = max(conterOne,maximumConsecutiveOne)
        counter += 1
    return maximumConsecutiveOne
    
"""
maxConsecutiveOnes - function that return maximumConsecuitive one
@array: List of binary number ( 0 or 1)
Return: return the maximum consecutive one

solution 2 | slide window technique
time complexity = 0(N)
space complexity = 0(1)
"""

def maxConsecutiveOnes(array):
    left = 0
    right = 0
    maximumConsectutiveOne = 0
    while right < len(array):
        if array[right] == 0:
            left = right + 1
        maximumConsecutiveOne = max(right - left + 1, maximumConsecutiveOne)
    return maximumConsecutiveOne
