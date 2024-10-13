"""Largest Number"""
def main(x,y,z):
    """main"""
    b = x+y+z
    c = x+z+y
    d = y+x+z
    e = y+z+x
    a = z+x+y
    f = z+y+x
    if int(a)>int(b):
        ma = int(a)
    else:
        ma = int(b)
    if ma<int(c):
        ma = int(c)
    if ma < int(d):
        ma = int(d)
    if ma < int(e):
        ma = int(e)
    if ma < int(f):
        ma = int(f)
    print(ma)
main(input(),input(),input())
