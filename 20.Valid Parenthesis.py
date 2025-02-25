#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#Approach 1:
class Solution:
    def isValid(self, s: str) -> bool:
      
      stack = []
      brackets = {')' : '(' , ']' : '[' , '}' : '{'}

      for char in s:
        if char in brackets.values():
            stack.append(char)
        elif stack and brackets[char] == stack[-1]:
          stack.pop()
        else:
          return False
        
      return stack == []

s = "({[]}"
a = Solution()
a.isValid(s)