"""Books"""
import math
def main(n,k,x,y):
    """main"""
    ans = 0
    still = k
    count = 0
    b = n
    for _ in range(n):
        still = k
        if math.ceil(k*(x/y))>=k:
            break
        count += 1
        while still>0:
            still -= math.ceil(k*(x/y))
            ans += 1
            x += 1
            y += 1
    ans += (b-count)
    print(ans)
main(int(input()),int(input()),int(input()),int(input()))
