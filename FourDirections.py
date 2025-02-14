"""FourDirections"""
def l(a):
    """l"""
    if a in (1,5):
        print("  *  ",end = " ")
    elif a in (2,4):
        print(" *   ",end = " ")
    elif a == 3:
        print("*****",end = " ")
def r(a):
    """r"""
    if a in (1,5):
        print("  *  ",end = " ")
    elif a in (2,4):
        print("   * ",end = " ")
    elif a == 3:
        print("*****",end = " ")
def main(x):
    """main"""
    for i in range(1,6):
        for j in x:
            if j == "U":
                if i == 2:
                    print(" *** ",end = " ")
                elif i == 3:
                    print("* * *",end = " ")
                elif i in (1,4,5):
                    print("  *  ",end = " ")
            elif j == "D":
                if i in (1,2,5):
                    print("  *  ",end = " ")
                elif i == 3:
                    print("* * *",end = " ")
                elif i == 4:
                    print(" *** ",end = " ")
            elif j == "L":
                l(i)
            elif j == "R":
                r(i)
        print()
main(input())
