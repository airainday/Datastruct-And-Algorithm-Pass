class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot1 TreeNode类
# @param pRoot2 TreeNode类
# @return bool布尔型
#
class Solution:
    def recursion(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 当一个节点存在另一个不存在时
        if root1 is None and root2 is not None:
            return False
        # 两个都为空则返回
        if root1 is None or root2 is None:
            return True
        # 比较节点值+递归比较子树
        return (
            root1.val == root2.val
            and self.recursion(root1.left, root2.left)
            and self.recursion(root1.right, root2.right)
        )

    def HasSubtree(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # write code here
        # 空树不是任何树的子树
        if pRoot2 is None or pRoot1 is None:
            return False
        # 递归比较
        flag1 = self.recursion(pRoot1, pRoot2)
        # 递归树1的每个节点
        flag2 = self.HasSubtree(pRoot1.left, pRoot2)
        flag3 = self.HasSubtree(pRoot1.right, pRoot2)

        return flag1 or flag2 or flag3
