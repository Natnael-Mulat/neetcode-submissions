class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        count = 0
        for i in nums:
            if i==0:
                count+=1
            else:
                pro*=i
        if count>1:
            return [0]*len(nums)
        
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if count:
                if nums[i] == 0:
                    ans[i] = pro
                else:
                    ans[i] = 0
            else:
                ans[i] = pro//nums[i]
        return ans


