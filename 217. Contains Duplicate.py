# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

#Approach 1:Sets

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set(nums)
        
        if len(hashset) == len(nums):
                return True
        else:
            return False

#Aprroach 2:Hash set Method

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    

nums = [1,4,5,7]
x = Solution()
x.containsDuplicate(nums)