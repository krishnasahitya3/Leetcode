#Approach 1

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1

        while start <= end:
            curr = numbers[start] + numbers[end]

            if curr > target:
                end -= 1
            elif curr < target:
                start += 1
            else:
                return [start+1, end+1]

        return []


numbers = [2,7,11,15]
target = 13
x = Solution()
x.twoSum(numbers,target)
