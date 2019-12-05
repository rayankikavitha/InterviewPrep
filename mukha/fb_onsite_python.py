"""
2) How do you calculate L7 ( given a input like this ?
output = { "mobile ": [1,1,1,1,0,1,1,], everything :[1,1,1,1,1,1,1]
       }

L7 is 7 days if a input is 1 in atleast one category, then 1 in the output.

 }

"""
input = { "android":[1,1,0,0,0,1,0] ,
              "ios":[1,0,1,1,0,0,1],
           "laptop":[0,0,0,0,1,1,0]
       }

category = {"mobile": ["ios","android"]
               ,"everything" : ["ios","android","laptop"] }

def cal_L7( input, category):
 	output = {}
 	for k,v in category.items():
 		for each_v in v:
 			if k not in output:
 				output[k] = input[each_v]
 			else:
 				output[k] = list(map(max,output[k],input[each_v]))

 	return output

print (cal_L7(input,category))


 		



