def solution(A, K):
    # An empty array stays empty after any number of rotations.
    if not A:
        return A

    # A full cycle of rotations leaves the array unchanged.
    K %= len(A)
    if K == 0:
        return A

    # Move the last K elements to the front.
    return A[-K:] + A[:-K]

