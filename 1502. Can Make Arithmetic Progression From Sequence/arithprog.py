class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort() #sort the array

        common_diff = arr[1] - arr[0] #define common difference

        for i in range(1, len(arr)-1): #define range
            if arr[i+1] - arr[i] != common_diff: #define condition for evaluating array elements
                return False
            
        return True
