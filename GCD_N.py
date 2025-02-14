"""GCD_N"""
def gcd(a, b):
    """gcd"""
    while b:
        a, b = b, a % b
    return a
def main(n):
    """main"""
    if n == 1:
        print(int(input()))
    else:
        lis = [int(input()) for _ in range(n) ]
        ans = lis[0]
        for i in range(1, len(lis)):
            ans = gcd(ans, lis[i])
        print(ans)
main(int(input()))
