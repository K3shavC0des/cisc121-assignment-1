def solution(A):
    # A permutation of length N contains each integer from 1 through N.
    values = set(A)
    if len(values) != len(A):
        return 0

    for number in range(1, len(A) + 1):
        if number not in values:
            return 0
    return 1

