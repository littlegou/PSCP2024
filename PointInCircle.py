"""PointInCircle"""
def main(x,y):
    """main"""
    r = int(input())
    xn = int(input())
    yn = int(input())
    ans = (((xn-x)**2)+((yn-y)**2))**(1/2)
    if ans<=r:
        print("True")
    else:
        print("False")
main(int(input()),int(input()))
