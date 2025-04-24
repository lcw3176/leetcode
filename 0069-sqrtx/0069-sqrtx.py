class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2, x + 1):
            if i * i > x:
                return i - 1

        return x