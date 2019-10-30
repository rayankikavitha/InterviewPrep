"""
Question: Given an arbitrary ransom notes and an another string containing all the
contents of all the magazies, write a function taht will return true if the ransom note
can be made from the magazines; otherwise, it will return false. 

Remember: every letter found in the magazines string can only be used once in your ransom note


For example: If the ransom test string was "no scheme" and the magaize string 
was "Programming interviews are weird", you would return false since you cann't format the first string by
grabbing and rearranging letters from the second string

string = "import" -> true for above 
"""

def make_ransom_note(note,magazine):
	d={}
	i,j=0,0
	while i < len(note) and j < len(magazine):
		if note[i] not in d:
			d[magazine[j]] = d.get(magazine[j],0) + 1
			j += 1
		else:
			d[note[i]] -= 1
			i += 1
		if i == len(note) :
			return True
		print (d)
	return False

print (make_ransom_note("import","programming interviews are weird"))
print (make_ransom_note("no scheme","programming interviews are weird"))
