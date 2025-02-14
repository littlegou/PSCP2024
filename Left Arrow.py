""" Left Arrow """
def main():
    """ Left Arrow """
    k = int(input())
    n = int(input())
    for i in range(n//2,0,-1):
        for _ in range(i,0,-1):
            print(" ",end = "")
        print("*"*k,end = "")
        print()
    print("*"*k)
    for i in range(1,(n//2)+1,+1):
        for _ in range(0,i,+1):
            print(" ",end = "")
        print("*"*k,end = "")
        print()
main()
