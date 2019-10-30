"""
Given a list of menu items and prices print all combinations that match a target price
target = 3
menu = {'A':1,'B',2}
output = [ ['A','A','A'],[A,B]]


"""
def combinationSum(c,t):
	dp =[[ [] for i in range(len(c))] for j in range(t+1)]
	print (dp)
	for n in range(1,t+1):
		for i, a in enumerate(c):
			if n == a:
				dp[n][i].append([a])
				print (dp)
			else:
				if n-a < 0: continue
				for b in dp[n-a][i:]:
					for s in b:
						dp[n][i].append([a,*s])
						print (dp)

	return [s for b in dp[-1] for s in b]




print (combinationSum([1,2],3))
	
