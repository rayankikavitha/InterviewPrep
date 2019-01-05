class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        while A:
            while A.next and A.next.val == A.val:
                A.next = A.next.next
            A = A.next
        return head