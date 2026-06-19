class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w = 0, 0
        while r<len(nums):
            if nums[r]!=0:
                nums[w] = nums[r]
                r+=1
                w+=1
            else:
                r+=1
        for i in range(w,len(nums)):
            nums[i]=0
        