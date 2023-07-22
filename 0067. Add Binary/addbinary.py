class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            bit_a = int(a.pop()) if a else 0
            bit_b = int(b.pop()) if b else 0
            
            current_sum = bit_a + bit_b + carry
            carry = current_sum // 2
            current_sum %= 2
            
            result.append(str(current_sum))
        
        return ''.join(result[::-1])
