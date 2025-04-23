class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_value = int(a, 2)
        b_value = int(b, 2)

        sum_bin = a_value + b_value
        
        return str(bin(sum_bin)).replace("0b", "")