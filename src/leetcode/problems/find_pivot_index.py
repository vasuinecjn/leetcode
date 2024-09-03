class Solution:

    def pivotIndex(self, nums: list[int]) -> int:
        prefix, postfix, l, r = 0, 0, 0, len(nums)-1
        left_sums, right_sums = [0] * len(nums), [0] * len(nums)

        while l < len(nums):
            prefix = 0 if l == 0 else prefix + nums[l-1]
            left_sums[l] = prefix
            l += 1
            postfix = 0 if r == len(nums)-1 else postfix + nums[r+1]
            right_sums[r] = postfix
            r -= 1
        for i, (l, r) in enumerate(zip(left_sums, right_sums)):
            if l == r:
                return i
        return -1


print(Solution().pivotIndex([2,1,-1]))
