# reverse_sentence_in_place.py

def reverse_str(word,left,right):
    while left < right:
        word[left],word[right]=word[right],word[left]
        left +=1
        right -=1
        


def reverse_words(message):
    
    reverse_str(message,0,len(message)-1)

    # Decode the message by reversing the words
    start =0
    for i in xrange(len(message)+1):
        if 
        (i == len(message)) or (message[i]==' '):
            reverse_str(message,start,i-1)
            start = i+1
    print message
   
    



print (reverse_words(list('the cat jumped over the dog')))
