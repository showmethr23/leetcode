class Solution:
    ddef maxProfit(sef, prices: List[int]) -> int:
        
        # Solution 1 -> Brute-Force Solution

        max_profit = 0
        
        for buy in range(len(prices)-1): # we do not need to buy in a last day
            for sell in range(buy+1, len(prices)):
                profit = prices[sell] - prices[buy]

                if profit > max_profit:
                    max_profit = profit
        return max_profit



