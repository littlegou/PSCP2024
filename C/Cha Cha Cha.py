"""Cha Cha Cha"""
import math
def main():
    """main"""
    day = int(input())
    ans = 0
    for _ in range(day):
        hr = float(input())
        hr = math.ceil(hr)
        ans += hr * 8720
    print(int(ans))
main()
