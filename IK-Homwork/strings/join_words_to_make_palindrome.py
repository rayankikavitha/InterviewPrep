"""
given = [ 'bat','tab','cat'], bat and tab can be comibed to form a palindrome
given = [ab,deedba] can be joined to form a palindrome
return the first one found

"""

def join_words(words):
    """
    :param input:
    :return:
    """
    d={}
    result =[]
    values=[]
    for i,word in enumerate(words):
        d[word[::-1]] = i
    #print d
    for i,word in enumerate(words):
        for j in range(len(word)+1):

            prefix = word[:j]
            postfix = word[j:]
            #print prefix, postfix

            if prefix in d and d[prefix] != i and postfix == postfix[::-1]:
                #print "first",prefix, postfix
                result.append((i,d[prefix]))
            if j > 0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                #print "second",prefix, postfix
                result.append((d[postfix], i))

    for each in result:
        values.append((words[each[0]], words[each[1]]))
    return values,result

given1 = [ 'bat','tab','cat']
given2 = ['ab','deedba']
given3 = ['geekf', 'geeks', 'or','keeg', 'abc', 'bc'];
print (join_words(given1))
print (join_words(given2))
print (join_words(given3))







