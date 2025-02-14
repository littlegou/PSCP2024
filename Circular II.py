"""Circular II"""
def main():
    """main"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())
    r2 = float(input())
    ans = (((xn-x)**2)+((yn-y)**2))**(1/2)
    if r+r2>ans:
        print("Yes")
    else:
        print("No")
main()
