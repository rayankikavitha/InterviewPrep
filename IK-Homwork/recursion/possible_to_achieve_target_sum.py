"""
Given an array of of size n and target sum k,
find out if there exists group of numbers ( not contigous) such that their sum is k
constraints 1<n<18 , -10**17 < k < +10**17
"""
def check_if_sum_possible(arr, k):
    """
    Returns True or False
    :param arr:
    :param k:
    :return:
    """
    return sum_possible(arr,len(arr),k)


def sum_possible(A,n,k):
    """
    :param A: Array set
    :param n: size of array
    :param k: sum k
    :return:
    """
    # Base Cases
    if (k == 0):
        return True
    if (n == 0 and k != 0):
        return False

    # If last element is greater than
    # sum, then ignore it for positive k
    if k > 0:
        if (A[n - 1] > k):
            return sum_possible(A, n - 1, k)
    else:
        if (A[n-1]  < k):
            return sum_possible(A,n-1, k)

    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return sum_possible(A, n - 1, k) or sum_possible(A, n - 1, k - A[n - 1])


print check_if_sum_possible([2,4,8],6)
print check_if_sum_possible([2,4,8],5)
print check_if_sum_possible([-1,4,6,9,-2,-3],8)
print check_if_sum_possible([-1,4,6,9,-2,-3],-6)


