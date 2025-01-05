class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j=n-1
        k=m+n-1
        if i==-1:
            i+=1
            for t in nums2:
                nums1[i]=t
                i+=1
            
        else:
            while i>=0 and j>=0:
            
                if nums1[i] > nums2[j]:
                    nums1[k]=nums1[i]
                    nums1[i]=0
                    k=k-1
                else:
                    nums1[k] = nums2[j]
                    j-=1
                    k-=1
                    i+=1
                    print(i)
                i-=1
            if i<0 and j>=0:
                
                for p in range (i+1, j+1):
                    nums1[p]=nums2[p]
