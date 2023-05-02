from typing import List

def signFunc(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product*=num
        return signFunc(product)
