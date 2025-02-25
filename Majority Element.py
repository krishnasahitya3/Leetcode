#Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

#Approach 1   
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a = {}
        result, maxcount = 0, 0
        
        for n in nums:
                a[n] = 1+ a.get(n, 0)
                result = n if a[n] > maxcount else result
                maxcount = max(a[n], maxcount)
        
        return result
          
          
nums = [3,2,3]
x = Solution()
x.majorityElement(nums)
        