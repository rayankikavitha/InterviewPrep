

def water_with_2_variables(A):
	water = 0
	lo, hi = 0, len(A)-1
	result = 0
	leftmax, rightmax = 0, 0
	while lo < hi:
		if A[lo] < A[hi]:
			if A[lo] > leftmax:
				leftmax = A[lo]
			else:
				result += leftmax - A[lo]
			lo += 1
		else:
			if A[hi] > rightmax:
				rightmax = A[hi]
			else:
				result += rightmax - A[hi]
			hi -= 1
	return result