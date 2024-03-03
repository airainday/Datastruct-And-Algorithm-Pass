def exist(board, word):
    if not board: return False

    rows = len(board)
    cols = len(board[0])
    # 构建一个矩阵，标志board中元素访问状态
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(i, j, index):
        # 深度优先遍历
        if index == len(word):  # index表示当前正在匹配的word中字符的索引
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or board[i][j] != word[index]:
            return False

        visited[i][j] = True  # 说明当前字符是匹配到了

        # 递归判断上下左右字符与word中下一个字符是否匹配
        if dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1):
            return True

        # 如果都行不通，将当前board中的字符设置为未访问过，以方便其他路径进行访问
        visited[i][j] = False

        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False


if __name__ == "__main__":
    # 示例用法
    board = [
    ['a','b','c','e'],
    ['s','f','c','s'],
    ['a','d','e','e']
    ]
    word1 = "bcced"
    word2 = "abcb"
    print(exist(board, word1))  # 输出 True
    print(exist(board, word2))  # 输出 False

        
