def solution(A):
    # Paired equal values cancel when XOR is applied.
    unpaired = 0
    for value in A:
        unpaired ^= value
    return unpaired
