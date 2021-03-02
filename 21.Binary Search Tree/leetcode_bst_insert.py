# Insert into a Binary Search Tree
# Description
""" 
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them. 

Exmaple1 :
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

https://leetcode.com/problems/insert-into-a-binary-search-tree/

"""

class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int):
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root