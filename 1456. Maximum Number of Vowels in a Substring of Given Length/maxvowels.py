class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'} #hash set
        
        l, cnt, res = 0, 0, 0 
        '''
        where:
        l - left pointer 
        cnt - count 
        res - result
        '''
        for r in range(len(s)): # r stands for right ponter

            cnt += 1 if s[r] in vowel else 0 
            # where r-l+1 = length of the window at hand
            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0 
                l += 1  
            res = max(res, cnt)
        return res

'''
Note - 
# Two pointers - Left and Right - keeps track of characters in substrings we iterate through in the given string. 
# Uses Sliding Window algorithm for solving the code. 
'''
