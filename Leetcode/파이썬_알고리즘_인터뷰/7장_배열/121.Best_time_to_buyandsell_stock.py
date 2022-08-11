import sys


prices = [7, 1, 5, 3, 6, 4]

def my_best_time_to_sell(prices):

    min = sorted(prices)[0]
    max_profit = 0
    for j in range(len(prices)):
        if j > prices.index(min):
            profit = prices[j] - min

            if profit > max_profit:
                max_profit = profit

    return max_profit

# 문제가 있다.
# [2,4,1] 이경우에는 2를 예상하는데 0 이라는값이 나온다..
# Brute Force 방법을 피하려다가 답마져 틀려버렸다.


# 풀이 1
def maxProfit_01(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

# 풀이 2
def maxProfit_02(prices):
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


print(maxProfit_02(prices))