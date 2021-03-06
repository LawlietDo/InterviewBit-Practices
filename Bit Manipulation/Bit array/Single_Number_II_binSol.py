class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    max_len = len(bin(max(A))[2:])
	    output = 0
	    for i in range(max_len):
	        x = 1 << i
	        binCounts = 0
	        for j in range(len(A)):
	            if A[j] & x:
	                binCounts += 1
	        if binCounts % 3:
	            output = output | x
	    return output
