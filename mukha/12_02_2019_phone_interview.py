# Python
"""
1) given 2 lists, find the unique items from the two. Set union - set intersection
2) given a dictionary with key,values, and n find the nth highest from the dictionary
input ={'a':10,'b':50,'c':100, 'd':30} n = 2 ( 2nd highest) output = 'b'
input={'lll':10, 'aaa':10,'x':5} n = 1 output = aaa, if there are multiple values for a key return the first one 
3) given a list with lot of nones copy the previous values to none
input = [1,None,2,None,None, 3, None]
output = [1,1,2,2,2,3,3]
"""

#SQL
"""
1) % of  products low_fat_renewable vs rest -> case
2) percentage of products with single marketing channel vs the rest.
Single marketing channel is the one with marketing channels not having comma separted list -> case
3) % of transactions that happend on the beginning and the end of promotions vs the rest. -> case
"""

def find_highest(input_dict, n):
	values = sorted(input_dict.values())
	rev_dict={}
	for k,v in input_dict.items():
		if v not in rev_dict:
			rev_dict[v] =[k]
		else:
			rev_dict[v] += [k]

	for k,v in rev_dict.items():
		rev_dict[k] = sorted(v)

	return rev_dict[values[len(values)-n]][0]

print (find_highest({'lll':10, 'aaa':10,'x':5},1))
print (find_highest({'a':10,'b':50,'c':100, 'd':30},2))