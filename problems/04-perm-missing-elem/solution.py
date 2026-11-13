def solution(A):
    # The full permutation contains the integers from 1 through N.
    N = len(A) + 1
    expected_sum = N * (N + 1) // 2
    return expected_sum - sum(A)
