class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        i, ans = 1, 0
        while n > i * (i - 1) // 2:
            if (n - i * (i - 1) // 2) % i == 0:
                ans += 1
            i += 1
        return ans