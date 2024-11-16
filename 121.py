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






class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 0

        profit = 0

        while sell < len(prices)-1:
            sell += 1

            profit = max(profit, prices[sell] - prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell

        return profit






def func(dep,ret):
    pt_dep = 0

    min_temp = ret[-1]
    for pt_ret in range(len(ret)-1,-1,-1):
        min_temp = min(ret[pt_ret],min_temp)
        ret[pt_ret] = min_temp 
    
    min_price = dep[0]+ret[-1]
    for pt_dep in range(len(dep)):
        if pt_dep < len(ret)-1:
            min_price = min(min_price,dep[pt_dep]+ret[pt_dep+1])

    return min_price

dep = [1,2,3,4]
ret = [4,3,2,1]

print(func(dep,ret))



