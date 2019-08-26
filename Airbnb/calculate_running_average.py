def calc_avg( inum, prev_sum=0, prev_cnt=0):
	cur_avg = (prev_sum.next()+inum)/ (prev_cnt.next()+1)
	prev_sum = prev_sum+inum
	prev_cnt+=1
	print(cur_avg)
	yield prev_sum, prev_cnt
	


input=[2,3]
go=calc_avg(x for x in input)
for each in go:
	print(each)





