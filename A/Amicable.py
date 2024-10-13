"""Amicable"""
def cal(n):
    """cal"""
    a = 0
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            a += i + int(n/i)
    return a + 1
def main(n):
    """main"""
    ans = 0
    for i in range(n,0,-1):
        f = cal(i)
        if f<=i:
            g = cal(f)
        else:
            continue
        if f != g and g == i :
            ans += f + g
    print(ans)
main(int(input()))
