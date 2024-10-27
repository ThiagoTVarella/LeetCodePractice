class Solution
    def maxProfit(self, prices List[int]) - int
        
        # Save the lowest I've seen with the maximum I've seen and compare profits

        profit = 0
        min = prices[0]

        for price in prices
            if price  min
                min = price
            if price-min  profit
                profit = price-min

        return profit