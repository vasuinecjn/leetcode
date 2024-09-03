class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) != len(word2):
            sl = len(word1) if len(word1) < len(word2) else len(word2)
        else:
            sl = len(word1)
        for j in range(sl):
            result += word1[j] + word2[j]
        result += word1[sl:] if len(word1) > len(word2) else word2[sl:]
        return result


print(Solution().mergeAlternately("vs", "au"))

