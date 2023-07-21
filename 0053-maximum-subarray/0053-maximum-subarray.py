class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxx=nums[0]
        currsum=0
        for i in nums:
            if currsum<0:
                currsum=0
            currsum=currsum+i    
            maxx=max(currsum,maxx)    
            
        return maxx      
        