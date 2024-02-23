class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self , preOrder, vinOrder):
        # write code here
        # 前序遍历第一个元素是根节点
        if len(preOrder) == 0:
            return None
        if len(preOrder) == 1:
            return TreeNode(preOrder[0])
        pRoot = TreeNode(preOrder[0])
        # 找到根节点在中序遍历列表里面的索引
        idx = vinOrder.index(preOrder[0])
        pRoot.left = self.reConstructBinaryTree(preOrder[1:len(vinOrder[:idx])+1], vinOrder[:idx])
        if 1+len(vinOrder[:idx]) == len(preOrder):
            pRoot.right = None
        else:
            pRoot.right = self.reConstructBinaryTree(preOrder[1+len(vinOrder[:idx]):], vinOrder[idx+1:])
        return pRoot
    
s = Solution()
res = s.reConstructBinaryTree([1,2,3], [2,1,3])
print(res.left.val)
