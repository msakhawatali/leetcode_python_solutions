class Solution(object):
    def sortColors(self, nums):

        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while mid<=high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid], nums[low]
                mid+=1 
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid] = nums[mid], nums[high]
                high -= 1
        return nums