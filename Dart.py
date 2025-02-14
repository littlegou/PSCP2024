"""Dart"""
import math
def cal(n):
    """cal"""
    if n <= 2:
        return 5
    if n <= 4:
        return 4
    if n <= 6:
        return 3
    if n <= 8:
        return 2
    if n <= 10:
        return 1
    return 0
def main():
    """main"""
    look = int(input())
    ans = 0
    for _ in range(look):
        x = input().split()
        r = math.sqrt((int(x[0])**2)+(int(x[1])**2))
        ans += cal(r)
    print(ans)
main()
