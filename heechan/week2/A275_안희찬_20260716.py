class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            left = i + 1
            right = n - i
            odd_count = (left * right + 1) // 2
            total += arr[i] * odd_count
        return total