input =[[1,2,3],[4,5,6,7],[[8,9]],[10,11,[12,13],14]]
output = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def flatten(input):
    r=[]
    for each in input:
        if type(each) ==  list:
            r += flatten(each)
        else:
            r.append(each)
    return r


print flatten(input)