class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = []
        lst.extend(nums1)
        lst.extend(nums2)
        lst.sort()

        if len(lst) % 2 == 0:
            return (lst[(len(lst) // 2) - 1] + lst[(len(lst) // 2)]) / 2

        return lst[(len(lst) // 2)]