# * Problem Statement * #

# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
    # has the same function as the code block of code above ↑

    # listOddInt = []
    # for i in range(len(seq)):
    #     soma = 0
    #     for num in seq:
    #         if seq[i] == num:
    #             soma+=1
    #
    #     if (soma%2)!=0:
    #         listOddInt.append(seq[i])
    #
    # for i in set(listOddInt):
    #     return i