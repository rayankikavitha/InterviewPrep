"""print one_edit_away('pale','ple')
print one_edit_away('pales','pale')
print one_edit_away('pale','bale')
print one_edit_away('pale','bake')
"""

def one_edit_away(str1,str2):
	if len(str1) == len(str2):
		# cases when one character replaced. pale, pall. or pale, pake
		if len(set(str1).intersection(set(str2))) == len(str1)-1 or len(set(str1).intersection(set(str2))) == len(str1)+1:
			return True
	elif len(str1) == len(str2)+1:
		# case when one character got added
		if set(str1).intersection(set(str2)) == set(str2):
			return True
	elif len(str2) == len(str1)+1:
		# case when one character got dropped
		if set(str1).intersection(set(str2)) == set(str1):
			return True
	else:
		return False


print (one_edit_away('pale','pall'))
print (one_edit_away('pale','pake'))