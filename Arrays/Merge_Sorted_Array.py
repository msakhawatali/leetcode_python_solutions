class Solution(object):
    def merge(self, nums1, m, nums2, n):
        idx = m+n-1
        i = m-1
        j = n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                idx -= 1
                i -= 1
            else:
                nums1[idx] = nums2[j]
                idx -= 1
                j -= 1
        while j >= 0:
            nums1[idx] = nums2[j]
            idx -= 1
            j -= 1