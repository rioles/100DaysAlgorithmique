"""
    solution 1
    checkPermutation - function that check if two string are permutation
    @string1: first string
    @string2: second string
    Return: return True if they are permutation otherwise False
    space 0(1)
    Time O(nlogn + mlogm)
"""
def checkPermutation(string1, string2):
    if(len(string1) != len(string2):
        return False
    str1 = sorted(string1)
    str2 = sorted(string2)
    for i in range(0,len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


"""
    solution 2
    checkPermutation - function that check if two string are permutation
    @string1: first string
    @string2: second string
    Return: return True if they are permutation otherwise False

    Time O(n)
    space 0(n)
"""
def checkPermutation(string1, string2):
    if(len(string1) != len(string2):
        return False
    hachMap = {}
    for i in range(0,len(string1)):
        hachMap[string1[i]] = i
    for j in range(0,len(string2)):
        if string2[j] not in hachMap:
            return False
    return True
