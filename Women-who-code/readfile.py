"""
"""

def readfile(filein):
	f =open(filein,'r+')
	next(f)
	for line in f:
		fields = line.split(',')
		
		yield fields
		

print (next(readfile('temporary.csv')))
print (next(readfile('temporary.csv')))
print (next(readfile('temporary.csv')))
print (next(readfile('temporary.csv')))
print (next(readfile('temporary.csv')))
