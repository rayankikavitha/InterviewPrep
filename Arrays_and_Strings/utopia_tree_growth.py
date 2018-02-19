def get_Height(input):
    length = 1
    if input == 0:
        return 1
    cycles = 1
    while cycles <= input:
        if cycles% 2 == 1:
            length = length * 2
        elif cycles % 2 == 0:
            length = length +1
        print "length =" + str(length)+" circles="+str(cycles)
        cycles = cycles + 1


    return length

print get_Height(3)
print get_Height(4)
print get_Height(5)
print get_Height(6)
