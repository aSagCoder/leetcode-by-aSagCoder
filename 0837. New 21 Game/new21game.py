#sliding window problem - can be optimally solved by sliding window + DP w/o TLE
#keep track of window sum!!!
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0: # or k +maxPts <= n:
            return 1.0
        windowSum = 0 
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0
        #cache - hashmap
        dp = {}  # start at score -> probability
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)            #dp[i + maxPts] - might not exist 
            windowSum += dp[i] - remove
        return dp[0]
