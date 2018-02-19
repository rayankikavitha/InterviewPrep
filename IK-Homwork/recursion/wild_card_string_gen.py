"""
1?0?

? acts as 0 or 1

How can you output using recursion

1101, 1100, 1001,1000

http://www.geeksforgeeks.org/wildcard-character-matching/

"""

def wild_card(input):
    # start with the first character
    wild_card_helper(list(input),0)

def wild_card_helper(input, i):

    if len(input) == i:  # print the output
        #print input
        print ''.join(input)
        return

    if input[i] == '?':  # encountered wildcard
        input[i] = '0'
        wild_card_helper(input,i+1)
        input[i] ='1'
        wild_card_helper(input,i+1)
        input[i] = '?'
    else:
        wild_card_helper(input,i+1)

print wild_card('1?0?')