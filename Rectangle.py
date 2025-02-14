"""Rectangle"""
def area(x,y):
    """area"""
    return x*y
def perimeter(x,y):
    """Perimeter"""
    return 2*(x+y)
def main(h,w):
    """main"""
    print(area(h,w))
    print(perimeter(h,w))
main(int(input()),int(input()))
