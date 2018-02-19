"""
https://stackoverflow.com/questions/7153659/find-an-integer-not-among-four-billion-given-ones?rq=1

Given an input file with four billion integers, provide an algorithm to generate an integer which is not contained in the file.
Assume you have 1 GB memory. Follow up with what you would do if you have only 10 MB of memory.


The size of the memory is 1GB 10 ** 9 9 bytes
File size is : 16 GB, here it is : input file is 4 billion, integers.. so 4 * 10 ** 9 * (4 bytes) = 16GB
Integers are 2 **32 =  4*10 pow 9


If they are 32-bit integers (likely from the choice of ~4 billion numbers close to 2^32),
 your list of 4 billion numbers will take up at most 93% of the possible integers (4 * 10^9 / (2^32) ).
 So if you create a bit-array of 2^32 bits with each bit initialized to zero
 (which will take up 2^29 bytes ~ 500 MB of RAM; remember a byte = 2^3 bits = 8 bits),
 read through your integer list and for each int set the corresponding bit-array element from 0 to 1;
 and then read through your bit-array and return the first bit that's still 0.

In the case where you have less RAM (~10 MB), this solution needs to be slightly modified.
 10 MB ~ 83886080 bits is still enough to do a bit-array for all numbers between 0 and 83886079.
  So you could read through your list of ints; and only record #s that are between 0 and 83886079 in your bit array.
   If the numbers are randomly distributed; with overwhelming probability (it differs by 100% by about 10^-2592069) you will find a missing int).
In fact, if you only choose numbers 1 to 2048 (with only 256 bytes of RAM) you'd still find a missing number an overwhelming percentage (99.99999999999999999999999999999999999999999999999999999999999995%) of the time.

But let's say instead of having about 4 billion numbers; you had something like 2^32 - 1 numbers and less than 10 MB of RAM;
so any small range of ints only has a small possibility of not containing the number.
If you were guaranteed that each int in the list was unique, you could sum the numbers and subtract the sum with one # missing to the full sum (1/2)(2^32)(2^32 - 1) = 9223372034707292160 to find the missing int.
However, if an int occurred twice this method will fail.

However, you can always divide and conquer. A naive method, would be to read through the array and count the number of numbers that are in the first half (0 to 2^31-1) and second half (2^31, 2^32).
Then pick the range with fewer numbers and repeat dividing that range in half. (Say if there were two less number in (2^31, 2^32) then your next search would count the numbers in the range (2^31, 3*2^30-1), (3*2^30, 2^32).
Keep repeating until you find a range with zero numbers and you have your answer. Should take O(lg N) ~ 32 reads through the array.

That method was inefficient. We are only using two integers in each step (or about 8 bytes of RAM with a 4 byte (32-bit) integer).
 A better method would be to divide into sqrt(2^32) = 2^16 = 65536 bins, each with 65536 numbers in a bin.
Each bin requires 4 bytes to store its count, so you need 2^18 bytes = 256 kB. So bin 0 is (0 to 65535=2^16-1), bin 1 is (2^16=65536 to 2*2^16-1=131071), bin 2 is (2*2^16=131072 to 3*2^16-1=196607).
In python you'd have something like:
"""


import numpy as np
nums_in_bin = np.zeros(65536, dtype=np.uint32)
print nums_in_bin
for N in four_billion_int_array:
    nums_in_bin[N // 65536] += 1
for bin_num, bin_count in enumerate(nums_in_bin):
    if bin_count < 65536:
        break # we have found an incomplete bin with missing ints (bin_num)

del nums_in_bin # allow gc to free old 256kB array
from bitarray import bitarray
my_bit_array = bitarray(65536) # 32 kB
my_bit_array.setall(0)
for N in four_billion_int_array:
    if N // 65536 == bin_num:
        my_bit_array[N % 65536] = 1
for i, bit in enumerate(my_bit_array):
    if not bit:
        print bin_num*65536 + i
        break