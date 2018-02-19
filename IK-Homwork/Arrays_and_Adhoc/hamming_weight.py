def printCountOfBitsSet(intArr):
    result = 0
    for each in intArr:
        result += str(bin(each)).count('1')
    return result
