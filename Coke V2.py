"""Coke"""
def main(a,b,c,d):
    """Coke"""
    if b and a != c:
        if not d%b:
            ans = (d*a) - (((d//b)-1) * (a-c))
        else:
            ans = (d*a) - ((d//b) * (a-c))
    else:
        ans = d*a
    if not d:
        ans = 0
    print(ans)
main(int(input()),int(input()),int(input()),int(input()))
