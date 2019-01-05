# find_avg_from_streaming_numbers
# Returns the new average 
# after including x 
def getAvg(newnum, n, sum): 
    sum = sum + newnum; 
    return float(sum) / n; 
  
# Prints average of a  
# stream of numbers 
def streamAvg(arr): 
	
    avg = 0
    n=len(arr)
    sum = 0
    for i in range(n): 
        avg = getAvg(arr[i], i + 1, sum)
        sum = avg * (i + 1)
        print "Average of " + str(i+1) + "st number is " + str(avg)
    return
  
# Driver Code 
arr= [ 10, 20, 30,  
       40, 50, 60 ]; 

streamAvg(arr); 