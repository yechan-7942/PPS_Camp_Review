class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        
        for n in nums:
            if n != 0:
                nums[insert] = n
                insert += 1
        
        for i in range(insert, len(nums)):
            nums[i] = 0