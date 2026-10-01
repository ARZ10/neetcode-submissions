class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_size = len(nums)
        set_nums = set(nums)
        if len(set_nums) != nums_size:
            return True

        return False
        