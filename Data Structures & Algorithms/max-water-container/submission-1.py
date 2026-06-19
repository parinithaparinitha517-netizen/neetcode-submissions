class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums=heights
        left=0
        right=len(nums)-1
        maxarea=0
        while left<right:
          cap=min(nums[left],nums[right])*(right-left)
          maxarea=max(cap,maxarea)
          if nums[left]<nums[right]:
            left+=1
          else:
            right-=1  
        return maxarea