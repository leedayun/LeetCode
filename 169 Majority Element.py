import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count={}
        thrs=math.floor(len(nums)/2)

        for i in nums:
            key=str(i)
            if count.get(key) is None:
                count[key]=1
            else:
                count[key]=count[key]+1
            if count[key]>thrs:
                return i
