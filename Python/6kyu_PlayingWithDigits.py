# * Problem Statement * #

# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
#
# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:
#
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
#
# If it is the case we will return k, if not return -1.
#
# Note: n and p will always be given as strictly positive integers. 

def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += pow(int(i), p)
        p+=1

    if sum%n == 0:
        return sum/n
    else:
        return -1

    # has the same function as the code block of code above ↑

    # sum = 0
    # for i,number in enumerate(str(n)): ← usando o "enumerate" conseguimos percorrer a lista e receber a posição e valor dela juntas
    #   sum += pow(int(number),p+i)
