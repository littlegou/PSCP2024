"""Kangaroo"""
def main(a,b,c):
    """Kangaroo"""
    mi = min(a,b,c)
    ma = max(a,b,c)
    me = (a+b+c) - (mi+ma)
    count = 0
    while abs(ma - me) != 1 or abs(mi - me) != 1:
        if abs(me-mi) <= abs(ma-me):
            mi,me = me , me+1
        else:
            ma , me = me , me-1
        count += 1
    print(count)
main(int(input()),int(input()),int(input()))
