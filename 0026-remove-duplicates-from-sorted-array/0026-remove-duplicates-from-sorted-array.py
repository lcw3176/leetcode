class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        lst = []

        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
                lst.append(i)

        nums.clear()
        nums.extend(lst)

        return len(lst)