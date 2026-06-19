class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 #this keeps track of the valid cases, so that we can replace them inplace
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[count] = nums[i]
                count+=1
        return count