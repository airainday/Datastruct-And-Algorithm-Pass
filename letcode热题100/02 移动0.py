
class Solution:
    def moveZeroes_(self, nums) -> None:
        """
        复制数组
        """
        n = len(nums)
        if n==1: return nums
        nums_ = [i for i in nums if i != 0]
        # 统计0的个数
        zeros = [i for i in nums if i== 0]
        nums_zero = len(zeros)
        nums_.extend(zeros)

        return nums_
    
    def moveZeroes(self, nums) -> None:
        """
        原地修改
        """
        # 双指针
        left = 0
        for right in range(len(nums)):
            # 如果right不为0则换到左侧
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
    

s = Solution()
res = s.moveZeroes([0,1,0,3,12])
print(res)