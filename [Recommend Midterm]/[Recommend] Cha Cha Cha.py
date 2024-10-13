"""[Recommend] Cha Cha Cha"""
import math
def main(n):
    """main"""
    ans = 0
    for _ in range(n):
        ans += math.ceil(float(input()))*8720
    print(ans)
main(int(input()))
