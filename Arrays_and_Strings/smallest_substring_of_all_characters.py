"""
input k =[x,y,z] and string = "xyyzyzyx"
output = "zyx"
"""

def uniquesubstr(arr,str):
    headIndex = 0
    result = []
    uniqueCounter = 0
    countMap = {}
    minlen = 0

    # initialize countMap
    for each in arr:
        countMap[each] = 0

    #scan str
    for i in range(len(str)):
        if str[i] in countMap and countMap[str[i]] == 0:
            countMap[str[i]] =1
            uniqueCounter += 1
            if uniqueCounter == 3 and:
                result.append(str[headIndex:i+1])
                countMap[str[headIndex]] = 0
                headIndex += 1


    if len(result) == 0:
        return ""
    else:
        for each in result:
            curlen = len(each)
            if curlen < minlen:
                minlen = curlen
                minstr = each
        return minstr



def cleardict(d):
    for k, v in d.items():
        d[k] = 0





print uniquesubstr("xyz","xyyzyzyx")