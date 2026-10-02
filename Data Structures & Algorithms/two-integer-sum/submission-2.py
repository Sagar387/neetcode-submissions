class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap tp see if the number taken you got from list - target in hashmap. If it is then good you return in the indcies if not then you keep going

        map = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff],i]
            map[num] = i

    