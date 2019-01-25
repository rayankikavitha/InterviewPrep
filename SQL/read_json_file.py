#!/usr/bin/env python
#coding=utf-8
import json
#import unicode_literals
#import requests
# curl https://bertha.va.opower.it/v2/executions/1748124  -o nov_pher_second.json

total = {}
def read_berth_job(filename):
	result ={}
	with open(filename, 'r') as f:
	        datastore =  json.load(f)
	#print datastore
	metric_details =  datastore['response']['berthaStepExecutions'][0]['berthaMetrics']
	for metric in metric_details:
		metricname = metric['metricName']
		count = metric['longValue']
		if metricname[:19] == 'eligibility.failure':
			result[metricname] = result.get(metricname,0) + count
			total[metricname] = total.get(metricname,0) + count
 	return result
		


print read_berth_job("/Users/kavitha.rayanki/nov_eher_first.json")
print read_berth_job("/Users/kavitha.rayanki/nov_eher_second.json")
print read_berth_job("/Users/kavitha.rayanki/nov_eher_third.json")
print read_berth_job("/Users/kavitha.rayanki/nov_eher_fourth.json")
print "Total="
print total


