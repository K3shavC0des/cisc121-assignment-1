"""OddOccurrencesInArray: write your own solution below."""


def solution(A):
    # create a list to keep track of the seen elements
    seen = []
    # iterate through the input array
    for item in A:
        # check if the item is already in the seen list
        if item not in seen:
            #  if not, add it to the seen list
            seen.append(item)
        else:
            # if it is, remove it from the seen list
            seen.remove(item)
    # return the only element left in the seen list, which is the one that occurs an odd number of times
    return seen[0]




