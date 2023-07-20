class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ss=set(nums)
        sl=sorted(list(ss))
        for i in range(len(ss)):
            nums[i]=sl[i]
        
        return len(ss)
        