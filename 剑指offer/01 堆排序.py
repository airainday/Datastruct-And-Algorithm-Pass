class Solution:
    def GetUglyNumber_Solution(self , index: int) -> int:
        if index == 0:
            return 0
        factors = [2,3,5]
        mp = dict()
        # 小顶堆
        import heapq
        pq = []
        mp[1] = 1
        heapq.heappush(pq, 1)
        res = 0
        for i in range(index):
            # 每次取最小的
            res = pq[0]
            heapq.heappop(pq)
            for j in range(3):
                next = res * factors[j]
                # 只取未出现过的
                if next not in mp:
                    mp[next] = 1
                    heapq.heappush(pq, next)
        return res
    
s = Solution()
s.GetUglyNumber_Solution(7)