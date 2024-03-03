"""
定义一个函数 get_digit_sum 来计算一个数字的数位之和。
定义一个函数 movingCountDFS 来进行深度优先搜索，从起始位置 (0, 0) 开始，搜索所有符合条件的格子。
在搜索过程中，判断当前位置是否越界、是否已经访问过、以及数位之和是否符合条件。
如果当前位置符合条件，将其标记为已访问，并继续向四个方向进行深度优先搜索。
最终返回所有符合条件的格子数目。
"""

def movingCount(rows, cols, threshold):
    def get_digit_sum(num):
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    
    def movingCountDFS(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or get_digit_sum(i) + get_digit_sum(j) > threshold:
            return 0

        visited[i][j] = True
        count = 1
        count += movingCountDFS(i+1, j)
        count += movingCountDFS(i-1, j)
        count += movingCountDFS(i, j+1)
        count += movingCountDFS(i, j-1)  
        return count

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    return movingCountDFS(0, 0)


# 示例用法
rows = 3
cols = 3
threshold = 2
print(movingCount(rows, cols, threshold))  # 输出 6
          