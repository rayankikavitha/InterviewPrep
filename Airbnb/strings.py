"""
print lcs("pwwkew")
Longest substring with non-repeating characters
"""

def longest_substring_with_no_repetition(given):
	visited = []
	maxlen = 0
	start = 0
	for i, v in enumerate(given):
		if v  in visited and start <= visited[v]:
			start = visited[v]+1
			
		else:
			maxlen = max(maxlen, i-start +1)
			
		visited[v] = i 
	return maxlen

	



"""
Remove duplicate from a list
"""

def nums(nums):






"""
Question 4:
 
Derive 312211 from 13112221
And from 13112221 to 312211 

1
11
21
1211
111221
312211
13112221

"""




"""
Irene :  s1 =”28”, s2 =”43” 
 Multiply s1*s2 , character by character

"""
def add_two_large_numbers(num1, num2):

	result = []
	carry = 0
	
	if len(num1) != len(num2):
		pad_num, non_pad_num = (num1,num2) if len(num1) < len(num2) else (num2, num1)
		pad_length = abs(len(num1) - len(num2))
		new_num1 = list(reversed('0'*pad_length + pad_num))
		new_num2 = list(reversed(non_pad_num))
	else:
		new_num1 = list(reversed(num1))
		new_num2 = list(reversed(num2))

	for i in range(len(new_num1)):
		digit = (int(new_num1[i]) + int(new_num2[i])) % 10 + carry
		carry = (int(new_num1[i]) + int(new_num2[i])) // 10
		result.append(str(digit))
	return ''.join(reversed(result))


print (add_two_large_numbers ('989','400555'))
	











"""
S1  =[4,5,1,2,3]
S2 = [5,1,2,3,6]
Output = [4,6]
Modification = how to spit out indexes [0,4]
Modification2 = if the numbers are repeating , how do you ?
     S1 = [ 4,4,5,1,2,3]  s2 = [5,1,2,3,6,6], output = {4:2, 6:2 }
"""
def first(s1, s2):
	result = []
	result += list(set(s1) - set(s2)) + list(set(s2) - set(s1))
	return result
def second(s1, s2):
	d =   {}
	for i,v in enumerate(s1):
		d[v] = i 
	for i,v in enumerate(s2):
		if v in d:
			del d[v]
		else:
			d[v] = i 
	return d

def third(s1, s2):
	d = {}
	for i,v in enumerate(s1):
		d[v] = d.get(v,0) + 1
	print (d)
	for i,v in enumerate(s2):
		if v in d:
			d[v] -= 1
	for i,v in enumerate(s2):
		if not (v in d and d[v] == 0):
			d[v] = d.get(v,0) +1 

	print (d)
	for k,v in list(d.items()):
		if v == 0:
			del d[k]
		
	return d






S1  =[4,5,1,2,3]
S2 = [5,1,2,3,6]
print (first(S1,S2))
print (second(S1,S2))
print ('---------begin--------')
print (third([4,4,5,1,2,3] , [5,1,2,3,6,6]))

print ('---------end--------')




# add digits
def add_digits(num):
	tot_sum = 0
	while num > 9:
		while num > 0:
			tot_sum += num%10
			num = num/10
		num = tot_sum
	return tot_sum
#print (add_digits(198))




# add one 
# given [9]  output [1,0]
# given [7,8,9] output [7,9,0]
# given [9,9,9] output [1,0,0,0]
def addone(nums):
	for i in range(len(nums)-1,-1,-1):
		if nums[i] < 9:
			nums[i] += 1
			return nums
		nums[i] = 0
	nums.insert(0,1)
	return nums


#print (addone([7,8,8]))
#print (addone([9,9,9]))
#print (addone([6,9,9]))
#print (addone([6,4,9]))


			
		
		  	




"""
substring problem o(m+n)

find pattern t in the string s
t = 'GACGCCA' s = 'CGC'
Appraoch define has function A = 0, C = 1, G = 2 etc
look for has match so CGC = 121
"""
import functools
def find_substring(s,t):
	
	if len(s) > len(t):
		return -1

	base = 26
	# hascodes for s and t[0:3]
	# reduce(function, iterable, initializer)
	t_hash= functools.reduce(lambda h,c : h * base+ord(c), t[:len(s)], 0) 
	s_hash = functools.reduce(lambda h,c : h * base+ord(c),s,0)
	power_s = base**max(len(s) -1, 0)
	print (t_hash)
	print (s_hash)
	# start from 3 rd position for the above example
	for i in range(len(s),len(t)):
		if t_hash == s_hash and t[i - len(s):i] == s:
			return i-len(s)  # found the match first

		# use rolling hash to compute the hash code
		t_hash -= ord(t[i-len(s)]) * power_s
		t_hash = t_hash * base + ord(t[i])
		print (t_hash)
	# tries to match s and t[-len(s):]
	if t_hash == s_hash and t[-len(s):] == s:
		return len(t) - len(s)
	return -1

print (find_substring('CGC','GACGCCA'))






"""
decoding and encoding

"""
# input = "3e4f2e"  -> output = 'eeeffffee'
def decoding(s):
	result = []
	for c in s:
		if c.isdigit():
			count = int(c)
		else:
			result.append(c*count)
			count = 0
	return ''.join(result)

#print (decoding('3e4f2e'))

# 'eeeffffee'"  -> output = 3e4f2e


def encoding(s):
	result =[]

	for i in range(len(s)-1):
		count = 1
		while s[i] == s[i+1]:
			count +=1

		result.append(str(count)+s[i])
	return ''.join(result)

#print (encoding('eeeffffeeg'))


		






# snake string
def snake(s):
	result = []
	for i in range(1,len(s),4):
		result.append(s[i])
	for i in range(0,len(s),2):
		result.append(s[i])
	for i in range(3,len(s),4):
		result.append(s[i])
	return ''.join(result)

def snake_pythonic(s):
	return s[1::4]+s[::2]+s[1::4]

print (snake('Hello world'))


"""
Compute all valid IP addresses

def is_valid_part(s):
	return  len(s) == 1 or (s[0] != '0' and int(s) < 255)

def get_valid_ip_addresses(s):

	for i in range(len(s)-1):
		if is_valid_part(s[i])	
		"""	







"""
Roman to integer
"""
roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
def roman_to_interger(s):
	tot = 0
	for i in range(len(s)-1):
		if s[i] < s[i+1]:
			tot -= roman[s[i]]
		else:
			tot += roman[s[i]]

	return tot+roman[s[-1]]

print (roman_to_interger('LIX'))

"""
Look and say 

"""
def next_number(s):
	result, i = [], 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i+1]:
			count += 1
			i += 1
		
		result.append(str(count)+s[i])
		i += 1
	return ''.join(result)

def look_and_say(n):
	s='1'
	for _ in range(1,n):
		s=next_number(s)
	return s

print (look_and_say(5))

#using python itertools.groupby
"""
>>> [print (k,v) for k,v in itertools.groupby(k)]
2 <itertools._grouper object at 0x109ea4518>
3 <itertools._grouper object at 0x109ea4588>
4 <itertools._grouper object at 0x109ea45c0>
[None, None, None]
>>> [print (k, list(v)) for k,v in itertools.groupby(k)]
2 ['2', '2', '2', '2']
3 ['3', '3', '3', '3', '3']
4 ['4', '4', '4', '4']
[None, None, None]
>>> [print (len(v),k) for k,v in itertools.groupby(k)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
TypeError: object of type 'itertools._grouper' has no len()
>>> [print (len(list(v)), k) for k,v in itertools.groupby(k)]
4 2
5 3
4 4
"""
import itertools
def next_number(s):
	s = ''.join(str(len(list(group)))+k for k,group in itertools.groupby(s))
	return s
print (next_number('1112223333'))







# ~x is equivalent to (-x) - 1.
# https://stackoverflow.com/questions/8305199/the-tilde-operator-in-python
"""
i  ~i  
0  -1
1  -2
2  -3
3  -4 
4  -5 
5  -6
"""
def is_palindrome(s):
	return all( s[i] == s[~i] for i in range(len(s)//2))

#print (is_palindrome('madam'))
#print (is_palindrome('clothes'))

import functools
# string to int
def str_to_int(s):
	running_sum = 0
	sign = [-1 if s[0] =='-' else 1][0]
	if s[0] != '-':
		s = '+'+s
	j = 1
	for i in range(1,len(s)):
		running_sum = running_sum * 10 + (ord(s[i]) - ord('0'))*j
		print (running_sum)
	#for i in range(len(s)-1, 0, -1):
	#	running_sum = running_sum + (ord(s[i]) - ord('0'))*j
	#	j = j * 10
	
	return running_sum*sign

#print (str_to_int('123'))

#print (atoi('-65469999999999999999999999999954'))

def int_to_string(x):
	is_negative = False
	if x < 0 :
		x,is_negative = -x,True
	s=[]
	while True:
		s.append(chr(ord('0') + x % 10))
		x = x //10
		if x == 0:
			break

	return ('-' if is_negative else '')+''.join(reversed(s))


#print (int_to_string(123))
#print (int_to_string(-45454))

def is_palindrome_sentence(sen):
	i,j = 0, len(sen) -1 
	while i < j:
		while not sen[i].isalnum() and i < j:
			i +=1
		while not sen[j].isalnum() and i < j:
			j -=1
		if sen[i].lower() != sen[j].lower():
			return False
		i,j = i + 1, j - 1
	return True

#print (is_palindrome_sentence('Kavitha you are awesome'))
#print (is_palindrome_sentence('Kavitha     isi ahtivaK'))

# Reverse all the words in a string


def reverse_words(s):
	

	def reverse_range(s,start,end):
		while start < end:
			s[start],s[end] = s[end],s[start]
			start, end = start+1, end -1

	# convert to array	and use it as string assignment is immutable
	tlist = list(s)
	reverse_range(tlist,0,len(s) - 1)

	start = 0
	while True:
		end = s.find(' ',start)
		if end < 0:
			break
		reverse_range(tlist,start,end -1 )
		start = end + 1

    # reverses the last word
	reverse_range(tlist,start,len(s)-1)
	return ''.join(tlist)


print (reverse_words('kavitha is awesome'))


