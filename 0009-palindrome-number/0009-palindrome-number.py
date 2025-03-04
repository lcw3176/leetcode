class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        value = list(str(x))

        if len(value) == 1:
            return True

        middle_index = int(len(value) // 2)
        one = []
        
        for i in range(0, middle_index):
            if value[i] != value[len(value) - 1 - i]:
                return False

        return True
            
