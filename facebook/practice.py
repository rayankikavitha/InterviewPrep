
import csv
#import os
import pandas
import glob

# This is not unit tested. 

class file_parsing:
	def __init__(self, directory_full_path):
		self.indiv_sparse_reports_=[]   # to create sparse reports
		self.global_sparse_reports_=[]  # to create sparse reports
		self.frame=pd.DataFrame[]  # to store all the records in the csv file
		
		if directory_full_path is None:
			print "provide valid directory"
			return
		else :
			allFiles = glob.glob(path + "/*.csv")
			frame = pd.DataFrame()
			list_ = []
			for file_ in allFiles:
    			df = pd.read_csv(file_)
    			df['file_name'] = file_  # append file name as a column
    			list_.append(df)  
			self.frame = pd.concat(list_)

	def calculate_individual_sparsity_report(self):
		return self.frame.groupby['file_name'].mean().transpose()
		

	def calculate_global_sparsity_report(self):
		return self.frame[].mean().transpose()


if __name__ == '__main__':
	fs = file_parsing("sample_director")
	print fs.calculate_global_sparsity_report()
	print fs.calculate_individual_sparsity_report()