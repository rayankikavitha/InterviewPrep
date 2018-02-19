input = ['opts','foo','bar','tops','pots','rab','ofo','hat']
output = [ ['opts','tops','pots'],['rab','bar'],['ofo','foo'],['hat']]
def anagram_sets(input):
    d={}
    for each in input:
        s=sorted(each)
        ss = ''.join(ch for ch in s)
        if ss in d:
            d[ss].append(each)
        else:
            d[ss] = [each]
    print d
    anagram_bucket =[]
    for k,v in d.iteritems():
        anagram_bucket.append(v)
    print anagram_bucket

anagram_sets(input)

x='a'
print

