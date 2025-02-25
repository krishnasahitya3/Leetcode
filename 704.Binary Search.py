#Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            m = (low+high)//2
            if nums[m] < target:
                low = m+1
            elif nums[m] > target:
                high = m-1
            else:
                return m
            
        return -1        
         
nums = [-1,0,3,5,9,12]
target = 5
x = Solution()
x.search(nums,target)