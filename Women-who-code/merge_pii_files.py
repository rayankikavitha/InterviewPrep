import pandas as pd
import sys



def date_to_month(val):
	calendar={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
	#print (val)
	month = str(val[4:6])
	#print (month)
	return calendar[month]

def add_current_cost(val):
	return val+'_current_cost'

def add_expected_cost(val):
	return val+'_expected_cost'

def add_diff_cost(val):
	return str(val)+'_cost_difference'

def create_pivot_file(infile):
	df = pd.read_csv(infile, sep='\t', error_bad_lines=False)
	# separate total and bill_period rows
	pii_df_curr  = df[(df.record_type == 'TOTAL') & (df.current_plan == 'Y')]
	pii_df_exp  = df[(df.record_type == 'TOTAL') & (df.current_plan == 'N')]
	curr_df = df[(df.record_type == 'BILL_PERIOD') & (df.current_plan == 'Y')]
	exp_df = df[(df.record_type == 'BILL_PERIOD') & (df.current_plan == 'N')]

	# manipulate header row and derive new rows
	pii_df_curr.rename(columns={"rate_plan_id": "current_rate_plan_id","total_cost":"current_plan_total_cost"},inplace=True)
	pii_df_exp.rename(columns={"rate_plan_id": "expected_rate_plan_id","total_cost":"expected_plan_total_cost"},inplace=True)
	print (pii_df_curr.head())
	print (pii_df_exp.head())
	pii_df_exp = pii_df_exp.filter(items = ['account_ID','expected_rate_plan_id','expected_plan_total_cost'])
	pii_df = pd.merge(pii_df_curr, pii_df_exp, how = 'inner', on=['account_ID'])
	print (pii_df.head())


	# transform the periods
	curr_df['month'] = curr_df['bill_period_end_date'].map(date_to_month)
	exp_df['month'] = exp_df['bill_period_end_date'].map(date_to_month)

    # select interested columns
	curr_df = curr_df.filter(items = ['account_ID','bill_period_cost','month'])
	exp_df = exp_df.filter(items = ['account_ID','bill_period_cost','month'])


	# make a new dataframe for calculating difference
	curr_df.rename(columns={"bill_period_cost": "bill_period_cost_curr"},inplace=True)
	exp_df.rename(columns={"bill_period_cost": "bill_period_cost_exp"},inplace=True)

	diff_df = pd.merge(curr_df,exp_df, how ='inner', on=['account_ID','month'])
	diff_df['bill_period_cost_diff'] = diff_df['bill_period_cost_curr'] - diff_df['bill_period_cost_exp']
	diff_df = diff_df.filter(items = ['account_ID','bill_period_cost_diff','month'])
	
	# change month lables by attaching related text
	curr_df['month_name'] = curr_df['month'].map(add_current_cost)
	exp_df['month_name'] = exp_df['month'].map(add_expected_cost)
	diff_df['month_name'] = diff_df['month'].map(add_diff_cost)

	# pivot the tables 
	curr_df = curr_df.pivot_table(index = 'account_ID',columns = 'month_name', values = 'bill_period_cost_curr')
	exp_df = exp_df.pivot_table(index = 'account_ID',columns = 'month_name', values = 'bill_period_cost_exp')
	diff_df = diff_df.pivot_table(index = 'account_ID',columns = 'month_name', values = 'bill_period_cost_diff')
	# print
	#print (curr_df.head())
	#print (exp_df.head())
	#print (diff_df.head())
	# merge all data frames 

	temp_dfs =  [pii_df,curr_df,exp_df,diff_df]
	final_df = functools.reduce(lambda left,right: pd.merge(left,right,on='account_ID'), temp_dfs)
	print (final_df.head())
	
	#print (final_df.head())
	# reorder column titles before writing
	columnsTitles = ['Analysis_date', 'account_ID', 'current_rate_plan_id','expected_rate_plan_id','current_plan_total_cost',
					 'expected_plan_total_cost','total_start_date', 'total_end_date','total_bill_periods', 'util_internal_id',
					 'customer_first_name',	'customer_last_name','mailing_address_line_1','mailing_address_line_2','mailing_address_line_3',
					  'mailing_address_line_4','Jan_current_cost','Jan_expected_cost','Jan_cost_difference',
					  'Feb_current_cost','Feb_expected_cost','Feb_cost_difference',
					  'Mar_current_cost','Mar_expected_cost','Mar_cost_difference',
					  'Apr_current_cost','Apr_expected_cost','Apr_cost_difference',
					  'May_current_cost','May_expected_cost','May_cost_difference',
					  'Jun_current_cost','Jun_expected_cost','Jun_cost_difference',
					  'Jul_current_cost','Jul_expected_cost','Jul_cost_difference',
					  'Aug_current_cost','Aug_expected_cost','Aug_cost_difference',
					  'Sep_current_cost','Sep_expected_cost','Sep_cost_difference',
					  'Oct_current_cost','Oct_expected_cost','Oct_cost_difference',
					  'Nov_current_cost','Nov_expected_cost','Nov_cost_difference',
					  'Dec_current_cost','Dec_expected_cost','Dec_cost_difference']
	final_df = final_df.reindex(columns=columnsTitles)
	final_df.to_csv('kr_testing.tsv', sep='\t',index=False)


create_pivot_file('brat_output.tsv')

	




	
"""
Sample data for 1 customer:

Analysis_date	account_ID	rate_plan_id	current_plan	default_plan	record_type	lowest_total_cost_plan	total_cost	total_start_date	total_end_date	total_bill_periods	bill_period_cost	bill_period_start_date	bill_period_end_date	has_errors	util_internal_id	customer_first_name	customer_last_name	mailing_address_line_1	mailing_address_line_2	mailing_address_line_3	mailing_address_line_4	service_address_line_1	service_address_line_2	service_address_line_3	service_address_line_4
20190813 130937	5010847224	MORG	Y	N	TOTAL	Y	1853	20180701 000000	20190731 000000	12				N	5012855486	DENNIS	BARNES	615 S CEDAR ST	DENNIS C BARNES	MICHELLE BARNESBELTON MO 64012-3044	615 S CEDAR ST	BELTON MO 64012-3044
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						151	20180711 000000	20180808 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						148	20180809 000000	20180909 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						99	20180910 000000	20181009 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						100	20181010 000000	20181107 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						230	20181108 000000	20181210 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						199	20181211 000000	20190109 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						265	20190110 000000	20190210 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						246	20190211 000000	20190312 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						106	20190313 000000	20190410 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						84	20190411 000000	20190512 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						95	20190513 000000	20190611 235959
20190813 130937	5010847224	MORG	Y	N	BILL_PERIOD						124	20190612 000000	20190711 235959
20190813 130937	5010847224	MORT	N	N	TOTAL	N	1854	20180701 000000	20190731 000000	12				N	5012855486	DENNIS	BARNES	615 S CEDAR ST	DENNIS C BARNES	MICHELLE BARNESBELTON MO 64012-3044	615 S CEDAR ST	BELTON MO 64012-3044
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						144	20180711 000000	20180808 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						139	20180809 000000	20180909 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						92	20180910 000000	20181009 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						99	20181010 000000	20181107 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						250	20181108 000000	20181210 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						203	20181211 000000	20190109 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						281	20190110 000000	20190210 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						263	20190211 000000	20190312 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						99	20190313 000000	20190410 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						77	20190411 000000	20190512 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						84	20190513 000000	20190611 235959
20190813 130937	5010847224	MORT	N	N	BILL_PERIOD						115	20190612 000000	20190711 235959
"""