# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

def mergeAlternately(self, word1: str, word2: str) -> str:
    sol=""
    i=0
    w1_len=len(word1)
    w2_len=len(word2)
    
    while i < w1_len or i < w2_len:
        if i < w1_len:
            sol += word1[i]
        if i < w2_len:
            sol += word2[i]
        i += 1

    return sol

"""
Discussion:
    This is a very straightforward question. we just want to merge s1 and s2 where we prioritize 
    s1.

    no tricks.
"""
