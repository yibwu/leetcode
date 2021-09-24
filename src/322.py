class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1] * (amount + 1)
        dp[0] = 0
        max_val = 1e4 + 1

        for n in range(1, amount+1):
            t = max_val
            for c in coins:
                if n == c:
                    t = 1
                    break
                elif n > c and dp[n-c] != -1:
                    t = min(t, dp[n-c]+1)
                else:
                    pass
            dp[n] = -1 if t == max_val else t
        return dp[amount]
 
