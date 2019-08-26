def transform_sample(nums):
	nums.sort()
	d={}
	for num in nums:
		key=str(num[0])+num[1]
		if key in d:
			d[key]+=([num[2],num[3]])
		else:
			d[key]=[num[2],num[3]]
	return d

print transform_sample(sample)

import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
import csv

calendar={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
def parse_brat(file):
	# create output files
	billperiod_t = open('brat_bill_period_current','r+')
	l=0
	dict_row={}
	with open(file,'r') as file_reader: 
	    for row in file_reader.readlines():
	    	curr_row = row.split('\t')
	    	customer_id = curr_row[2]
	    	current_plan = curr_row[3]
	    	record_type = curr_row[5]
	    	bill_period_cost = curr_row[11]
	    	period_start = curr_row[12]
	    	period_end = curr_row[13][4:6]
	    	if l == 0 :
	    		row = 'customer_id'
	    		row.append('')
	    		total_f.write(row)
	    	if record_type == 'TOTAL':
	    		total_f.write(row)
	    	elif record_type=='BILL_PERIOD' and record_type ='Y':
	    		writer.writerow({'customer_id': customer_id, calendar[period_end]+'_actual':bill_period_cost})
	    		if customer_id not in dict_row:
	    			custom_row = str(bill_period_cost)+','+calendar[period_end]
	    			dict_row[customer_id] = [custom_row]
	    		else:
	    			custom_row =str(bill_period_cost)+','+calendar[period_end]
	    			dict_row[customer_id].append(custom_row)

	    	l+=1	