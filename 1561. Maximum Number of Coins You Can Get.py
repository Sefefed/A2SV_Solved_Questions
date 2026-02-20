class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i = 1
        k = len(piles) // 3
        ans = 0
        times = 0
        i = 1
        while times < k:
            ans += piles[i]
            i += 2
            times += 1
        return ans


