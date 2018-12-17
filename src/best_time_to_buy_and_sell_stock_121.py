class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit

        buy_price = prices[0]
        sell_price = prices[0]
        max_profit = 0

        for p in prices[1:]:
            if p < buy_price:
                if sell_price > buy_price and sell_price - buy_price > max_profit:
                    max_profit = sell_price - buy_price
                buy_price = p
                sell_price = p
            else:
                if p > sell_price:
                    sell_price = p
                else:
                    t = sell_price - buy_price
                    max_profit = max_profit if max_profit > t else t
        if sell_price > buy_price:
            t = sell_price - buy_price
            max_profit = max_profit if max_profit > t else t
        return max_profit