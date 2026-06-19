class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if j!=i:
                    pro*=nums[j]
            ans[i] = pro
        return ans