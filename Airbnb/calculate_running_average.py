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

def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))



