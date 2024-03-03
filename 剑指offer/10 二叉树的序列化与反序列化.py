import sys
#设置递归深度
sys.setrecursionlimit(100000) 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = 0 
        self.s = ""

    #处理序列化（递归）
    def SerializeFunction(self, root):
        #空节点
        if not root:
            self.s += '#'
            return
        #根节点
        self.s += (str)(root.val) + '!'
        #左子树
        self.SerializeFunction(root.left) 
        #右子树
        self.SerializeFunction(root.right) 
    
    def Serialize(self, root): 
        if not root:
            return '#'
        self.s = ""
        self.SerializeFunction(root)
        return self.s
    
    #处理反序列化的功能函数（递归）
    def DeserializeFunction(self, s: str):
        #到达叶节点时，构建完毕，返回继续构建父节点
        #空节点
        if self.index >= len(s) or s[self.index] == "#": 
            self.index += 1
            return None
        # 数字转换
        val = 0
        #遇到分隔符或者结尾
        while s[self.index] != '!' and self.index != len(s):
            val = val * 10 + (int)(s[self.index])
            self.index += 1
        root = TreeNode(val)
        #序列到底了，构建完成
        if self.index == len(s): 
            return root
        else:
            self.index += 1
        #反序列化与序列化一致，都是前序
        root.left = self.DeserializeFunction(s)  
        root.right = self.DeserializeFunction(s)
        return root

    def Deserialize(self, s):
        if s == "#":
            return None
        return self.DeserializeFunction(s)
    

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(7)

    s = Solution()
    res = s.Serialize(root)
    s.Deserialize(res)

