class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # use the set function and compare lengths to see if duplicates
        # set function is O(n) tc

        distinct = set(nums)
        if len(distinct) == len(nums):
            return False
        else :
            return True
        