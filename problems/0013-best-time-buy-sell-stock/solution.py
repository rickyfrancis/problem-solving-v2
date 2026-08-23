# 121. Best Time to Buy and Sell Stock

from typing import List

def maxProfit(prices: List[int]) -> int:
               
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit 

    
    
    
prices = [7,2,5,3,6,4,1]

print(maxProfit(prices))