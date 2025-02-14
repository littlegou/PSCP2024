"""CompositeFunction"""
def f(x):
    """f(x)"""
    return 2*x
def g(x):
    """g(x)"""
    return x/2+1
def main(a):
    """main"""
    print(f"{f(g(a)):.2f}")
    print(f"{g(f(a)):.2f}")
main(int(input()))
