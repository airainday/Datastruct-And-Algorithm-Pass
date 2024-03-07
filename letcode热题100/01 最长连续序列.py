class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) <= 1: return len(nums)
        # 先排序
        nums.sort()
        # 再遍历
        temp = 1  # 记录所有连续序列长度
        res = []  # 记录每个temp

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                temp += 1
            # 防止重复元素发生
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                res.append(temp)
                temp = 1
        
        res.append(temp)  # 防止一直连续，没有经过else分支
        
        return max(res)
    
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,2,0,1]
s = Solution()
res = s.longestConsecutive(nums)
print(res)