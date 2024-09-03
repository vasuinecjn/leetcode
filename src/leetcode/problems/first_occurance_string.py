class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: len(needle) + i] == needle:
                return i
        return -1


print(Solution().strStr("vasuisgood", "vasuisgood"))

