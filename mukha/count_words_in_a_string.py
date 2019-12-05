given_string = "One two         three\n  four\tfive  "
def count_words(input):
    state = 'OUT'
    wc = 0
    for each_char in input:
        if each_char in (' ', '\n','\t'):
            state = 'OUT'
        elif state == 'OUT':
            wc += 1
            state = 'IN'
    return wc


given2 = "The Mission of the toast-master  is nothing but\n given. Mission of the toast-master"

print (count_words(given_string))
print (count_words(given2))

from collections import defaultdict

input1 = "The mission the mission the mission accomplished today."
def count_distinct_words(input):
    d = defaultdict(int)
    print (d)
    l = input.split()
    print (l)
    for each in l:
        d[each] += 1

    return [ k for k,v in d.items()]

print (count_distinct_words(input1))

#print (one_edit_away('pale','ple'))




