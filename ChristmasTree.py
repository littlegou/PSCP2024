""" ChristmasTree """
def main():
    """ main """
    n = int(input())
    k = int(input())
    for i in range(1,n+1):
        a = 1
        b = i-1
        for j in range(1,n+i):
            if j<= n-i:
                print(" ",end = "")
            else:
                if a<=i:
                    print("*",end = "")
                    a+=1
                else:
                    print("*",end = "")
                    b-=1
        print()
    for i in range(k):
        print(" "*(n-2)+"-"*3)
main()
