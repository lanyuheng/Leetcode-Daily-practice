from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个字典来存储数值和它们的索引
        num_to_index = {}
        
        # 遍历数组
        for index, num in enumerate(nums):
            # 计算当前数需要的配对数
            complement = target - num
            
            # 如果配对数已经在字典中，返回当前索引和配对数的索引
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # 如果配对数不在字典中，将当前数和索引加入字典
            num_to_index[num] = index
        
        # 如果没有找到符合条件的两个数，返回空数组
        return []

# 示例用法
solution = Solution()
