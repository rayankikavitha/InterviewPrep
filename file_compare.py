
import csv
import pandas as pd
def file_compare(file1,file2):
	dfwelcome = pd.read_csv(file1, sep='\t')
	dfreject = pd.read_csv(file1, sep='\t')
	print dfreject

file_compare('CPS_undeliverables.txt','CO-69899_CPS_welcome_letter_extract_opsqa (1).tsv')

