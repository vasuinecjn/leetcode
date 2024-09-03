class Solution:

    def romanToInt(self, s: str) -> int:
        # MCMXCIV
        p = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        result = 0
        for i in range(n):
            if i + 1 < n and p[s[i]] < p[s[i + 1]]:
                result -= p[s[i]]
            else:
                result += p[s[i]]
        return result


print(Solution().romanToInt("MCMXCIV"))


