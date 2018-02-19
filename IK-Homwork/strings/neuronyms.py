"""
given = "batch"
output = [ b3h, ba2h, b2ch]
until 2

given = "nailed"
output = [n4d, na3d, n3ed, nai2d, n2led, na2ed]

https://www.careercup.com/question?id=5733696185303040
"""


def make_all_str(input_str):
    result = []
    # adjust the range to get 1s
    for l in range(2, len(input_str)-2+1):
        for start in range(1, len(input_str) - l):
            #print start
            res_str = input_str[:start] + str(l) + input_str[(start + l):]
            result.append(res_str)
        # end loop
    # end loop
    #result.append(str(len(input_str)))
    return result


def do_the_thing(input_str):
    return map(lambda str: input_str[0] + str + input_str[-1], make_all_str(input_str[1:-1]))

print make_all_str("nailed")
print make_all_str("batch")
print(do_the_thing("internationalization"))
