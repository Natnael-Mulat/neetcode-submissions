class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftmax, rightmax = height[l], height[r]
        waters=0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                waters+= leftmax-height[l]
            else:
                r-=1
                rightmax = max(rightmax, height[r])
                waters+= rightmax - height[r]
        return waters

            
        