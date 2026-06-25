class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
      buy=0
      sell=1
      maxProfit=0
      for i in range(len(prices)-1):
       if(prices[buy]>prices[sell]):
          buy=sell
       else:
          maxProfit=max((prices[sell]-prices[buy]),maxProfit)
       sell+=1  
      return maxProfit      