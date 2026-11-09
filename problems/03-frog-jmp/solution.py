

def solution(X, Y, D):
    #initialize the starting position, ending position, and jump distance
    start = X
    end = Y
    jump_distance = D
    # iterate through the range of jumps from the starting position to the ending position with a step size of jump_distance
    for jumps in range(start, end, jump_distance):
        if jumps >= end:
            # if the current position is greater than or equal to the ending position, break the loop
            return jumps // jump_distance

