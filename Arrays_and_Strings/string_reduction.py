json_data =[{"exe": "bin1", "args": "-o /tmp"},
{"exe": "bin2", "args": ["-t myTest", "-v", "-o /tmp"]},
{"exe": "bin3", "args": [{"width": 640, "height": 480}]}
]
#
# Output example:
# bin1 -o /tmp
# bin2 -t myTest -v -o /tmp
# bin3 width 640 height 480

import shilpa_training

def flat_the_json(json_data):
    final_d = {}
    for each in json_data:
        for k, v in each.iteritems():
            if k == "exe":
                actual_key = each[k]
            if k == "args":
                actual_val = each[k]
                final_d[actual_key]=actual_val
    return final_d


final_d = flat_the_json(json_data)

for k, v in final_d.iteritems():
    if type(v) is str:
        print k, v
    if type(v) is list:
        if len(v) > 1 :
            print k, ' '.join(x for x in v if type(x) is str)
        else:
            newd = v[0]
            print k, ' '.join(x + ' ' +str(newd[x]) for x in newd)


"""
final_d = {'bin1': '-o /tmp', 'bin3': [{'width': 640, 'height': 480}], 'bin2': ['-t myTest', '-v', '-o /tmp']}
sd =[{'width': 640, 'height': 480},{'lenght':500}]
def flat_dict(d):
    result= ' '
    for each in d:
        result = result + ' '.join( [x + ' ' +str(each[x]) for x in each])+' '
    return result

print "output from flat dict"
print flat_dict(sd)
"""