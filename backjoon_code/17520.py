def pow_n(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    if n%2 > 0 :
        return pow_n(x, n-1)*x
    half = pow_n(x, n/2)
    half = half % 16769023
    return (half*half) % 16769023

n = int(input())

if n < 0:
    print("error")
    exit()

if n%2 == 0:
    result = pow_n(2, (n/2))
    print(result % 16769023)
elif n%2 == 1:
    result = pow_n(2, ((n+1)/2))
    print(result % 16769023)
