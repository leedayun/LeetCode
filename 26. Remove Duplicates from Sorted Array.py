class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cp=1
        k=1
        last=nums[0]
        dup = 0

        for i in range(1,len(nums)):
            if nums[i] == last and dup == 0:
                dup =1
  
            elif nums[i] != last:
                k+=1
                last=nums[i]
                nums[cp]=nums[i]
                dup=0
                cp+=1
        return k

