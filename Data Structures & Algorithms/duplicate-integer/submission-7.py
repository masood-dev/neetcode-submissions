class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # takes O(n) but in less code
        return len(nums) > len(set(nums))
