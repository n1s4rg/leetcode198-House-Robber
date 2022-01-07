from typing import List


class Solution:
    def helper(self, nums):
        cur = prev = 0
        for i in range(len(nums)):
            prev, cur = cur, max(cur, prev + nums[i])

        return cur

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_with_first_elem = self.helper(nums[:-1])
        max_with_last_elem = self.helper(nums[1:])

        return max(max_with_first_elem, max_with_last_elem)

c1 = Solution()
print(c1.rob([2,3,2]))