class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for digit in nums:
            my_set.add(digit)
        if len(my_set) == len(nums):
            return False
        else:
            return True


        
        