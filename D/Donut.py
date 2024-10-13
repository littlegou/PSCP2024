"""Donut"""
def cal(a,b,c,d):
    """main"""
    ans = 0
    al = 0
    ans += (d//(b+c))*a*b
    al += (b+c)*(d//(b+c))
    if (d%(b+c))-b>=0:
        ans += b*a
    else:
        ans += (d%(b+c))*a
    if (d%(b+c))-b>=0:
        al += b+c
    else:
        al += d%(b+c)
    print(f"{ans} {al}")
cal(int(input()),int(input()),int(input()),int(input()))
