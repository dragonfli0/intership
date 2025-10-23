#Наибольший общий делитель
def GCD(a,b):
    if a == 0 or b == 0:
        return max(a,b)
    return GCD(b, a%b)
a, b = map(int, input().split())
print(GCD(a,b))

#Наименьшее общее кратное
def LCM(a,b):
    return a*b//GCD(a,b)
a, b = map(int, input().split())
print(LCM(a,b))

#Наибольшее число шагов алгоритма Евклида
n = int(input())
a = 1
b = 1
while b <= n:
    a, b = b, a + b

before_prev = b - a  # это F_{k-1}
print(before_prev, a)
#Наименьшее число шагов алгоритма Евклида
