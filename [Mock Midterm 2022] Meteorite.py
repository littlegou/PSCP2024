"""Meteorite"""
def main(a,b,c):
    """Meteorite"""
    n = 0
    z = 0
    if a<c:
        print(0)
    else:
        while True:
            if a/b>=c:
                a /= b
                z += b**n
            else:
                z += b**n
                break
            n += 1
        print(z)
main(float(input()),int(input()),float(input()))
