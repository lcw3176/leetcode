class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst = [str(i) for i in digits]
        temp = list(str(int("".join(lst)) + 1))
        answer = [int(i) for i in temp]
        
        return answer