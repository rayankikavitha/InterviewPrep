def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
        print i
        print z
        print '*******'
    return z + roman[s[-1]]

input ='XXVI'
input2 = 'VLC'
print romanToInt(input)
print romanToInt(input2)