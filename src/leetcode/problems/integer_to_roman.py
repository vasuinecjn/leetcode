class Solution:

    def intToRoman(self, num: int) -> str:
        deci = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        index = 0
        while num > 0:
            if num >= deci[index]:
                result += rom[index]
                num = num - deci[index]
            else:
                index += 1
        return result


print(Solution().intToRoman(3749))




