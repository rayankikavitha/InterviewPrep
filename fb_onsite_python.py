"""
2) How do you calculate L7 ( given a input like this ?

input = { "android":[1,1,0,0,0,1,0] ,
              "ios":[1,0,1,1,0,0,1],
           "laptop":[0,0,0,0,1,1,0]
       }

 category = {. "mobile": ["ios","android"]
               ,everything = ["ios","android","laptop"]

 output = { "mobile ": [1,1,1,1,0,1,1,], everything :[1,1,1,1,1,1,1]
       }

L7 is 7 days if a input is 1 in atleast one category, then 1 in the output.

 }
 """

 def cal_L7( input, category):
 	output = {}, i = 0
 	for k,v in category:
 		



