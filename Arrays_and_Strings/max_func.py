temp=[90,100,75,60,80,102,63]
temp1=[100,43,62,107,78,105]

def max_function(temp):
    num=0
    for i in range(len(temp)):
        if(num<temp[i]):
            num=temp[i]
    return num

def min_function(temp):
    num=temp[1]
    for i in range(len(temp)-1):

        if num>temp[i]:
            num=temp[i]
    return num


def Avg_function(temp):
    avg=0
    sum=0
    for i in range(len(temp)):
        sum=sum+temp[i]
    avg=float(sum/len(temp))
    return avg

print "Avg",Avg_function(temp)
print "Avg",Avg_function(temp1)

print "max", max_function(temp)
print "min",min_function(temp)

print "max",max_function(temp1)
print "min",min_function(temp1)



