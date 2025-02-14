"""Milk"""
def main(n):
    """main"""
    x = 0
    num = []
    for _ in range(n):
        x = float(input())
        num.append(x)
    num.sort()
    if not n%2:
        ans = (float(num[int(((n+1)/2)-0.5)-1]) + float(num[int(((n+1)/2)+0.5)-1]))/2
    else:
        ans = float(num[int((n+1)/2)-1])
    print(f"{ans:.3f}")
main(int(input()))
