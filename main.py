def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= num_coins * coin
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] * (amount + 1)
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        min_coins[i] = float('inf')
        for coin in coins:
            if i >= coin and 1 + min_coins[i - coin] < min_coins[i]:
                min_coins[i] = 1 + min_coins[i - coin]
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Example usage:
print("Greedy Algorithm:", find_coins_greedy(113))
print("Dynamic Programming Algorithm:", find_min_coins(113))
