-class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        """ 
        Return maximum profit from list of stock prices

        Parameters:
        prices (list of int) is the list of stock prices

        Returns:
        int: maximum profit 

        This function will iterate over the list of prices. As it iterates, it will save the minumum, and compare each current price with the minimum, to find the maximum difference. It then returns that difference
        """
        # Create variables for temporary minimum and temporary maximum difference
        min_price = prices[0]
        max_profit = 0
        temp_profit = 0

        # Iterate over prices
        for price in prices:

            # Update minimum price
            if price < min_price:
                min_price = price

            # Update maximum profit
            temp_profit = price - min_price
            if temp_profit > max_profit:
                max_profit = temp_profit
        
        return max_profit
