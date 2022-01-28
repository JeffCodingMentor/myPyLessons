'''
LeetCode 13. Roman to Integer
'''
symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = len(s)-1
        while i>=0:
            if i>0 and symbol[s[i-1]] < symbol[s[i]]:
                res = res + symbol[s[i]] - symbol[s[i-1]]
                i-=1
            else:
                res += symbol[s[i]]

            i-=1
        return res