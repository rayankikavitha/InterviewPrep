def one_edit_away(s1,s2):
    # case when one character replaced.
    if len(s1)==len(s2):
        if (len(set(s1).intersection(set(s2)))==len(s1) - 1 or len(set(s1).intersection(set(s2)))==len(s1) + 1):
            return True
    # case when one character being added.
    if len(s1) == len(s2)+1 :
        if set(s1).intersection(set(s2)) == set(s2):
            return True
    # case when one character is removed.
    if len(s1) == len(s2) - 1:
        if set(s1).intersection(set(s2)) == set(s1):
            return True

    return False

print one_edit_away('pale','ple')
print one_edit_away('pales','pale')
print one_edit_away('pale','bale')
print one_edit_away('pale','bake')

