'''
Given n steps, find the number of ways to reach the nth staircase if you can only
climb 1, 2 or 3 steps at a time.
Solve in O(n) time and O(1) space.
Tags: Dynamic Programming, Recursion
Companies: N/A
'''

''' O(n) time and space '''
def possibleWays(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


    




