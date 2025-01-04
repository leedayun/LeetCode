class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0 #occurence 
        l=len(nums)-1
        i=0
        while i<=l:
            if nums[i] != val:
                k+=1
                i+=1
            elif nums[l] != val:
                nums[i]=nums[l]
                nums[l]=val
                i+=1
                l-=1
                k+=1
            else:
                l-=1
            
        return k
