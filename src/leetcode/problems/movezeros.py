class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        0,1,0,3,12
        """
        ip = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ip] = nums[i]
                ip += 1

        while ip < len(nums):
            nums[ip] = 0
            ip += 1


s = Solution()
lst = [0, 1, 0, 3, 12]
s.moveZeroes(lst)
print(lst)
