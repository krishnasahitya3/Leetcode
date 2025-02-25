class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None
     
a1=BinaryTreeNode(10)
a2=BinaryTreeNode(15)
a3=BinaryTreeNode(20)
a4=BinaryTreeNode(60)
a5=BinaryTreeNode(14)
a6=BinaryTreeNode(25)
a7=BinaryTreeNode(6)
 
a1.leftChild=a2
a1.rightChild=a3
a2.leftChild=a4
a2.rightChild=a5
a3.leftChild=a6
a3.rightChild=a7
 
print("Root Node is:")
print(a1.data)
 
print("left child of node is:")
print(a1.leftChild.data)
 
print("right child of node is:")
print(a1.rightChild.data)
 
print("Node is:")
print(a2.data)
 
print("left child of node is:")
print(a2.leftChild.data)
 
print("right child of node is:")
print(a2.rightChild.data)
 
print("Node is:")
print(a3.data)
 
print("left child of node is:")
print(a3.leftChild.data)
 
print("right child of node is:")
print(a3.rightChild.data)
 
print("Node is:")
print(a4.data)
 
print("left child of node is:")
print(a4.leftChild)
 
print("right child of node is:")
print(a4.rightChild)
 
print("Node is:")
print(a5.data)
 
print("left child of node is:")
print(a5.leftChild)
 
print("right child of node is:")
print(a5.rightChild)
 
print("Node is:")
print(a6.data)
 
print("left child of node is:")
print(a6.leftChild)
 
print("right child of node is:")
print(a6.rightChild)
 
print("Node is:")
print(a7.data)
 
print("left child of node is:")
print(a7.leftChild)
 
print("right child of node is:")
print(a7.rightChild)





def has_cycle(head):
    slow = head 
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


    
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

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
nums = [3,2,3]
b = sorted(nums)
print(b)


nums = [0,0,1]
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i <= (len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
            else:
                i +=1
 
nums = [0,0,1]
x= Solution()
x.moveZeroes(nums)

while i <= (len(nums)):
    if nums[i] == 0:
        nums.append(0)
        nums.pop(i)
    else:
        i +=1
               
print(nums)