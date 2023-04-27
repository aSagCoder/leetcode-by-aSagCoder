class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0 
        lps = [0] * len(needle)

        prevLPS, i = 0, 1

        while i < len(needle): #for setting LPS Array
            if needle[i] == needle[prevLPS]:
                #case 1 - prefix = suffix
                lps[i] = prevLPS + 1 
                prevLPS += 1 
                i += 1
            elif prevLPS == 0: #prevLPS is at index 0
                lps[i] = 0 
                i += 1 
            else:
                #if prefix is not equal to suffix
                prevLPS = lps[prevLPS - 1] 
        
        i = 0 #pointer for needle
        j = 0 #pointer for haystack
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1


#time complexity of KMP algorithm = O(n+m)
#time complexity for setting up LPS = O(2.n)
