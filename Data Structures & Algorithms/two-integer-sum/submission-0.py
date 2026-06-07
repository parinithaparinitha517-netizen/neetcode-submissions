class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            competent=target-nums[i]
            if competent in count:
                
                return [count[competent],i]
            count[nums[i]]=i    