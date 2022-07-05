class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_len = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                forward = num + 1
                while forward in nums:
                    forward += 1
                seq_len = max(seq_len, forward - num)
        return seq_len