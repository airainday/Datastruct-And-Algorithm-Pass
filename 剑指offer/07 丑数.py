class Solution:
    def GetUglyNumber_Solution(self , index: int):
        # write code here
        # 丑数的2,3,5倍都是丑数
        res = [1]
        i = 0
        while len(res) < index:
            temp = [res[i]*2, res[i]*3, res[i]*5]
            for j in temp:
                if j not in res:
                    res.append(j)
            i += 1
        return res[-1]


if __name__ == "__main__":
    s = Solution()
    res = s.GetUglyNumber_Solution(7)
    print(res)