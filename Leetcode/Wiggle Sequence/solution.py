class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = None
        seqLenght = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and seq != True:
                seq = True
                seqLenght += 1
            if nums[i] < nums[i+1] and seq != False:
                seq = False
                seqLenght += 1
        return seqLenght