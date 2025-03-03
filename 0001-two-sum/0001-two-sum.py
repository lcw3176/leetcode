class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(0, len(nums)):
            dic[i] = nums[i]

        reveresed_key = sorted(dic, reverse=True)

        for i in range(0, len(reveresed_key)):
            one = dic[reveresed_key[i]]

            for j in range(i + 1, len(reveresed_key)):
                two = dic[reveresed_key[j]]

                if one + two == target:
                    return [reveresed_key[j], reveresed_key[i]]
            
        return []