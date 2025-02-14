""" Right Arrow """
def main():
    """ Right Arrow """
    k = int(input())
    n = int(input())
    for i in range(0,(n//2),+1):
        for _ in range(0,i,+1):
            print(" ",end = "")
        print("*"*k,end = "")
        print()
    print(" "*(n//2)+"*"*k)
    for i in range(n//2,0,-1):
        for _ in range(i,1,-1):
            print(" ",end = "")
        print("*"*k,end = "")
        print()
main()
