class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Solution 1
        
        for i in range(n):
            nums1[i+m] = nums2[i]

        nums1.sort()


        # Solution 2
        # Using three pointers from the end

        # last index number for nums1
        last = m+n-1
        
        # compare and merge between nums1 and nums2
        # initial condition: two pointers are greater than 0
        while m > 0 and n > 0:
            # if nums1's last index number is greater than nums2's last index number
            if nums1[m-1] > nums2[n-1]:
                # nums1's last index should be replace the nums1[m-1]
                nums1[last] = nums1[m - 1]
                # update the pointer
                m -= 1
            # if nums1[m-1] < nums2[n -1]
            else:
                # put nums2's last index number into nums1 last index
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # for edge cases, if the smallest number is in nums2
        # elements should be left over in nums2
        # so we should try to put them into nums1 if there are
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

