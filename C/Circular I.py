"""Circular I"""
def main(x,y):
    """main"""
    r = float(input())
    xn = float(input())
    yn = float(input())
    ans = (((xn-x)**2)+((yn-y)**2))**(1/2)
    if ans<=r:
        print("Yes")
    else:
        print("No")
main(float(input()),float(input()))
