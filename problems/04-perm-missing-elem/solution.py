


def solution(A):
    #n should be the length of the array + 1, as one element is missing
    N = len(A) + 1
    #sum of first N natural numbers]
    total_sum = (N*(N+1))/2 #what the actual sum should be if all elements were there
    actual_sum = sum(A) #what the sum is, missing one element
    return (total_sum - actual_sum) #the value of that one element must be this

