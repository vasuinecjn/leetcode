class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_index = {}
        for i in range(len(nums)):
            if complement_index.get(nums[i], None) is not None:
                return [complement_index[nums[i]], i]
            complement_index[target - nums[i]] = i
        return nums


s = Solution()
print(s.twoSum([2,7,11,15], 9))
