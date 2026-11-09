
def solution(A, K):
    #Create a interal function to rotatel the array once
    def rotate(arr):
        #take the last element and store it as it will be the first element after rotation
        end = arr[-1]
        #shift all the elements to the right by one position
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        #set the first element to the last element stored in end
        arr[0] = end
    # Rotate the array K times
    for _ in range(K):
        rotate(A)
    # return the rotated array
    return A


#    TESTING
# -------------------
# A = [i for i in range(1,10)]
# print(A)
# print(solution(A, 3))
#  It Works
# Terminal Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [7, 8, 9, 1, 2, 3, 4, 5, 6]