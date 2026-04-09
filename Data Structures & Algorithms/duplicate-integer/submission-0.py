class Solution:
    def hasDuplicate(self, nums: List[1,2,3,3]) -> bool:
        return len(nums) != len(set(nums))
