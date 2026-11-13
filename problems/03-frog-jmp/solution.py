def solution(X, Y, D):
    # Round the remaining distance up to a whole number of jumps.
    distance = Y - X
    return (distance + D - 1) // D
