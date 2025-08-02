class Solution:
    def reverse(self, x: int) -> int:
        lst = []

        for i in reversed(str(x)):
            if i.isdigit():
                lst.append(i)
        
        result = int("".join(lst))

        
        if result >= 2 ** 31 - 1 or result <= -2 ** 31:
            return 0

        if x < 0:
            return -result

        return result 