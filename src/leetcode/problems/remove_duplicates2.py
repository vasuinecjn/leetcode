class Solution:
    # 0, 1, 1, 1, 1, 2, 2, 3, 3, 4
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1


print(Solution().removeDuplicates([1, 2, 2]))
