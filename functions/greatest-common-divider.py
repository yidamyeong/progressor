# 유클리드 호제법 최대공약수 계산
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
