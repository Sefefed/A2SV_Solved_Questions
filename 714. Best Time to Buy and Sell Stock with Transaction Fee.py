class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
            cash = 0
            held = float('-inf')
            for price in prices:
                cash = max(cash, held + price - fee)
                held = max(held, cash - price)
            return cash
