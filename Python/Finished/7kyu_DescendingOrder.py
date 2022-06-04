# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    # listOrderReverse = sorted(str(num), reverse=True)
    # numReverse = "".join(listOrderReverse)
    
    # has the same function as the line of code below ↓
    return int("".join(sorted(str(num), reverse=True)))
