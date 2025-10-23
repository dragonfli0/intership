#1, 5, 10, 20, 50
money = int(input())

def change(money):
    coins_used = []
    numCoins = 0
    while money>0:
        if money >= 50:
            money=money-50
            coins_used.append(50)
        elif money>=20:
            money=money-20
            coins_used.append(20)
        elif money>=10:
            money=money-10
            coins_used.append(10)
        elif money>=5:
            money=money-5
            coins_used.append(5)
        else:
            money = money - 1
            coins_used.append(1)
        numCoins += 1
    return numCoins, coins_used

min_coins, coins = change(money)

print(min_coins)
print(" ".join(map(str, coins)))
