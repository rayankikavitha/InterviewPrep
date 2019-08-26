sample=[[1, 'MORG', 50,'jan'], [1, 'MORG',50,'feb'],[2, 'MORG',50,'jan'], [2, 'MORG',50 ,'feb'], [2, 'MORT',50, 'jan'], [2, 'MORT',50 ,'feb']]

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
"""
analysis_date	account_ID	rate_plan_id	current_plan	default_plan	record_type	
lowest_total_cost_plan	total_cost	total_start_date	total_end_date	total_bill_periods	bill_period_cost	
bill_period_start_date	bill_period_end_date	has_errors	util_internal_id	customer_first_name	customer_last_name	
mailing_address_line_1	mailing_address_line_2	mailing_address_line_3	mailing_address_line_4	service_address_line_1
	service_address_line_2	service_address_line_3	service_address_line_4
	"""
log = open('brat_output.tsv')
def parse_log(log):
	newfile1 = open('brat_total.tsv','r+')
	newfile2 = open('brat_bill_period_current.tsv','r+')
	newfile3 = open('brat_bill_period_future.tsv','r+')
	#writer1 = csv.writer(newfile1,delimiter=',')
	#writer2=  csv.writer(newfile2,delimiter=',')
	#writer3=  csv.writer(newfile2,delimiter=',')
	for line in log:
		split_line = line.split('\t')
		#print split_line
		current_plan = split_line[3]
		record_type = split_line[5]
		#print current_plan, record_type	

        if record_type =='record_type':
        	newfile1.writelines(split_line)
        	newfile1.writelines(line)
        	newfile2.writelines(line)
        	newfile3.writelines(line)
        elif record_type =='TOTAL':
        	newfile1.writelines(line)
        	newfile1.writelines(split)
        elif record_type =='BILL_PERIOD' and current_plan =='Y':
        	newfile2.writelines(line)
        elif record_type =='BILL_PERIOD' and current_plan =='N':
        	newfile3.writelines(line)

	newfile1.close()
	newfile2.close()
	newfile3.close()
     
#parse_log(log)

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


def parse_brat(file):
	# create output files
	total_f = open('brat_total.tsv','r+')
	billperiod_current_f = open('brat_bill_period_current.tsv','r+')
	billperiod_future_f = open('brat_bill_period_future.tsv','r+')
	l=0
	with open(file,'r') as file_reader: 
	    for row in file_reader.readlines():
	    	curr_row = row.split('\t')
	    	current_plan = curr_row[3]
	    	record_type = curr_row[5]
	    	if l == 0 :
	    		total_f.write(row)
	    		billperiod_future_f.write(row)
	    		billperiod_current_f.write(row)
	    	if record_type == 'TOTAL':
	    		total_f.write(row)
	    	elif record_type=='BILL_PERIOD' and current_plan =='Y':
	    		billperiod_current_f.write(row)		
	    	elif record_type=='BILL_PERIOD' and current_plan =='N':
	    		billperiod_future_f.write(row)

	    	l+=1	

#parse_brat('brat_output.tsv') 


# merging files based on a key

import pandas as pd
def transpose(file):
	csv = pd.read_csv("test.csv", skiprows=1, sep='\t')
	df = pd.DataFrame(data=csv)
	transposed_csv = df_csv.T
	print transposed_csv

transpose('brat_bill_perid_current.tsv')

	   