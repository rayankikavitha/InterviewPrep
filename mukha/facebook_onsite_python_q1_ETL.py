"""
2) How do you calculate L7 ( given a input like this ?

input = { "android":[1,1,0,0,0,1,0] ,
              "ios":[1,0,1,1,0,0,1],
           "laptop":[0,0,0,0,1,1,0]
       }

 category = {. "mobile": ["ios","android"]
               ,everything = ["ios","android","laptop"] }
 output = { "mobile ": [1,1,1,1,0,1,1,], everything :[1,1,1,1,1,1,1]
       }
 if any day is 1, then populate 1 in the output.
"""
import collections as collections
from functools import reduce

def call7(input,category):
    #result=collections.defaultdict(list)
    result={}
    newresult={}
    for category_key,category_val in category.items():
        if category_key not in result:
            result[category_key] =[0]*7
            for each_category_val in category_val:
                #result[category_key]= list(zip(result[category_key],input[each_category_val]))
                result[category_key]= list(map(max,result[category_key],input[each_category_val]))

    print (result)

print(call7(input,category))



from collections import defaultdict

def calculate_L7(input, category):
	output = defaultdict(list)

	for cat_type,cat_val in category.items():
		#print cat_type, cat_val
		i = 0 
		curr_day_l7 = 0
		while i < 7:
			for each in cat_val:
				#print each,i
				curr_day_l7 = max(curr_day_l7,given[each][i])
			output[cat_type].append(curr_day_l7)
			i += 1
			curr_day_l7 = 0
	return output

given = { "android":[1,1,0,0,0,1,0] ,
              "ios":[1,0,1,1,0,0,1],
           "laptop":[0,0,0,0,1,1,0]}
category = { "mobile": ["ios","android"],"everything" : ["ios","android","laptop"] }
               


print calculate_L7(given,category)

