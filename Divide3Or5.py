"""Divide3Or5"""
def main():
    """man"""
    n = int(float(input()))
    ans = 0
    for i in range(1,n+1):
        if not i % 3:
            ans += i
        elif not i % 5:
            ans += i
    print(ans)
main()
