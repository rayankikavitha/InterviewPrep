

def squares(N):
    i = 0
    while True:  
        if i > N:
            raise StopIteration
        yield i*i
        i +=1

squared_values = [i for i in squares(20)]
print squared_values

log = open('example_log.txt')
def parse_log(log):
    for line in log:
        split_line = line.split()
        remote_addr = split_line[0]
        time_local = split_line[3]+" "+split_line[4]
        request_type = split_line[5]
        request_path = split_line[6]
        status = split_line[8]
        body_bytes_sent = split_line[9]
        http_referrer = split_line[10]
        http_user_agent = " ".join(split_line[11:])
        yield (
            remote_addr, time_local, request_type, request_path,
            status, body_bytes_sent, http_referrer, http_user_agent
        )
        
first_line = next(parse_log(log))
#print first_line
#second_line = next(parse_log(log))
# example_log.txt doesn't have second line.
#print second_line
                 
"""
Write a function build_csv() that takes in a required argument, lines (a list of parsed rows), and optional arguments header and file.
If there is a header argument, insert the header at the beginning of the parsed rows.
Write the CSV to the given file.
Return the file.
Open the file temporary.csv for reading and writing.
Call build_csv() with the following variables:
parsed for lines.
A list or tuple of the header names in the screen's example.
The temporary.csv file.
Assign the build_csv() return value to the variable csv_file.
Call csv_file.readlines() and assign the return value to the variable contents.
Print the first 5 rows of contents using print().
"""
import csv
log = open('example_log.txt')
parsed = parse_log(log)
def build_csv(lines,header= None,file=None):
    if header:
        lines = [header]+[l for l in lines]
    writer = csv.writer(file,delimiter=',')
    writer.writerows(lines)
    file.seek(0)
    return file

file = open('temporary.csv','r+')
csv_file = build_csv(parsed,
                     header=[
        'ip', 'time_local', 'request_type',
        'request_path', 'status', 'bytes_sent',
        'http_referrer', 'http_user_agent'
            ],
             file=file
                    )

contents = csv_file.readlines()
print contents[:2]                                                            
