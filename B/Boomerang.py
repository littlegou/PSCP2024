"""Boomerang"""
def main(x,y,z):
    """main"""
    x = int(x)
    y = int(y)
    z = int(z)
    print(f"{x+1}\n{7*y**3+2*y**2-31*y+1}\n{-z}\n{(x+y)*(x-y)}")
    print((y-(y**2-4*x*z)**(1/2))/(2*x))
main(input(),input(),input())
