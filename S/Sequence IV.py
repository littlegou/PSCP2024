"""Sequence IV"""
def main(x):
    """main"""
    for i in range(1,x+1):
        print(i,end=" ")
    print()
    for i in range(1,x):
        for j in range((x*i)+1,(x*i)+x+1):
            print(j,end=" ")
        print()
main(int(input()))
