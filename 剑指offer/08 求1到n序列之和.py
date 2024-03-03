class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        n > 1 and self.Sum_Solution(n-1)
        self.sum += n
        return self.sum
    

if __name__ == "__main__":
    s = Solution()
    sum = s.Sum_Solution(3)
    print(sum)
    print(3^-1)


