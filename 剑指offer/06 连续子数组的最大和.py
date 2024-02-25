# -*- encoding: utf-8 -*-
'''
@File    :   06 连续子数组的最大和.py
@Time    :   2024/02/26 07:33:03
@Author  :   rainday 
@Version :   1.0
@Description : 有一数组，求其连续子数组和的最大值
'''
class Solution:
    def sub_array_max_sum(self, nums):
        n = len(nums)
        if n<= 1: return nums
        # dp数组，储存长度从0到len(num_list)的数组的从未知位置到数组长度的子数组的最大值
        dp = [nums[0]]  
        res = nums[0]  # 记录整个数组的所有连续子数组和的最大值
        for i in range(1, n):
            if nums[i] + dp[i-1] > nums[i]:
                dp.append(nums[i] + dp[i-1])
            else:
                dp.append(nums[i])
            if dp[i] > res:
                res = dp[i]
        return res

if __name__ == "__main__":
    s = Solution()
    num_list = [1, -2, 3, 10, -4, 7, 2, -5]
    res = s.sub_array_max_sum(num_list)
    print(res)
            





        