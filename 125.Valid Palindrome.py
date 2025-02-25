#Approach 1:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start <= end:
            while start < end and not s[start].isalnum():
                start += 1
            while end>start and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

s = "A man, a plan, a canal: Panama"
s = "race a car"
x = Solution()
x.isPalindrome(s)
        
