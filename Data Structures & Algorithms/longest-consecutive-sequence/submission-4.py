class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for num in nums:
            current=num
            length=1
            if current-1 not in nums:
                current+=1
                
                while current in nums:
                 length+=1
                 current+=1
            longest=max(longest,length) 
        return longest       

        