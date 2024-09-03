class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i, j = 0, 0
        n = len(s)
        while i < n and j < n:
            while i < n and s[i] == " ": i += 1
            if i > n: break
            j = i
            while j < n and s[j] != " ": j += 1
            if i < n or j < n:
                result = s[i:j] if result == "" else s[i:j] + " " + result
            i = j
        return result.strip()


print(Solution().reverseWords("a"))


