#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#Approach 1:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

#Approach 2:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                        if nums[i]+nums[j] != target:
                            continue
                        return([i,j])
    



nums = [2,7,11,15]
target = 9
x = Solution()
x.twoSum(nums,target)



