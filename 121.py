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





        """
        Solution 2
        
        Using two variables

        1. create a float variable as infinity for minimum price
        2. create a int variable for maximum profit as an answer
        3. iterate the prices[i] to find which number is min_price and max_price
            1. if - condition: prices[i] < min_price, if price of stock is cheaper than my minimum price 
                1. swap the buying date as min_price = prices[i]
            2. elif - condition: prices[i] - min_price > max_profit, if my current max_profit is less than future selling stock price
                1. swap the selling date as max_profit = prices[i] - min_price
        4. return max_profit
        """

        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
