class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                result.append(str(start) if start == end else f"{start}->{end}")
                if i < len(nums):
                    start = nums[i]          

        return result