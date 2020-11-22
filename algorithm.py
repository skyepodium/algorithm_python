coin_types = [500, 100, 50, 10, 5, 1]

money = int(input())
remain = 1000 - money

result = 0

for coin in coin_types:
    result += remain // coin
    remain %= coin

print(result)