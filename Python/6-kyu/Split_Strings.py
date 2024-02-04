"""
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

    Examples:
        'abc' =>  ['ab', 'c_']
        'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    listS = []  
    for i in range(0, len(s), 2):
        if len(s[i:i+2]) == 1:
            listS.append(s[i] + '_')
        else:
            listS.append(s[i:i+2])

    return listS
