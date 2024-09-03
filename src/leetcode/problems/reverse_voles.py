class Solution:
    def reverseVowels(self, s: str) -> str:
        voles = "aeiouAEIOU"
        l, r = 0, len(s) - 1
        sl = [c for c in s]
        while l < r:
            if sl[l] not in voles:
                l += 1
                continue
            if sl[r] not in voles:
                r -= 1
                continue
            sl[l], sl[r] = sl[r], sl[l]
            l += 1
            r -= 1
        return "".join(sl)

print(Solution().reverseVowels("hello"))